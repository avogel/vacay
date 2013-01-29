from django.shortcuts import render
from django.template import Context
from django.http import HttpResponseRedirect
from vacay.vposts.models import *
from vacay.forms import BlogForm
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required
def blogging(request, id):
	try:
		id = int(id)
	except ValueError:
		raise Http404()
	try:
		trip = Trip.objects.get(id=id)
	except Exception, e:
		return HttpResponseRedirect('/home/')
	if not trip.user == request.user:
		return HttpResponseRedirect('/home/#blogModal')
	if request.method == 'POST':
		if 'fromTripPlanning' in request.POST:
			trip.is_completed = True
			trip.save()
			selected_date = -1
			form = BlogForm()
		elif 'fromBlogging' in request.POST:
			form = BlogForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				vd = cd['day']
				post = Post(title=cd['title'], contents=cd['contents'], date_written=date.today())
				post.save()
				vd.written_posts.add(post)
				vd.save()
				return HttpResponseRedirect('/blogging/%d/' % trip.id)
			try:
				selected_date = int(form['day'].value())
			except:
				selected_date = -1
		else:
			selected_date=-1
			form = BlogForm()
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

