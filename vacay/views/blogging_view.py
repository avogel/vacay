from django.shortcuts import render
from django.template import Context
from django.http import HttpResponseRedirect
from vacay.vposts.models import *
from vacay.forms import BlogForm
from datetime import date

def blogging(request, id):
	try:
		id = int(id)
	except ValueError:
		raise Http404()
	trip = Trip.objects.get(id=id)
	if request.method == 'POST':
		form = BlogForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			vd = cd['day']
			post = Post(title=cd['title'], contents=cd['contents'], date_written=date.today())
			post.save()
			vd.written_posts.add(post)
			vd.save()
			return HttpResponseRedirect('/vacay/blogging/%d/' % trip.id)
		try:
			selected_date = int(form['day'].value())
		except:
			selected_date = -1
	else:
		form = BlogForm()
		selected_date = -1
	cities = VisitedCity.objects.filter(trip=trip)
	days = {}
	for city in cities:
		ds = VisitedDay.objects.filter(visited_city=city)
		days[city]=ds
	return render(request, 'blogging.html', {'trip' : trip,
						'cities' : cities, 
						'days':days,
						'form': form,
						'selected_date' : selected_date})

