from django.template.loader import get_template
from django.http import Http404, HttpResponse
from django.shortcuts import *
from vacay.vposts.models import *
from django.utils import simplejson
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def viewpost(request, id):
	try:
		id = int(id)
	except ValueError:
		raise Http404()
	post = Post.objects.get(id=id)
	user = request.user
	if request.method == 'POST':
		type = request.POST["type"]
		bookmark_id = request.POST["id"]
		if type == 'trip':
			trip = Trip.objects.get(id=bookmark_id)
			trip.ideas.add(post)
			trip.save()
		elif type == 'city':
			city = VisitedCity.objects.get(id=bookmark_id)
			city.ideas.add(post)
			city.save()
		else:
			day = VisitedDay.objects.get(id=bookmark_id)
			day.ideas.add(post)
			day.save()
		return HttpResponse(simplejson.dumps())
	if user.is_authenticated():
		trips = Trip.objects.filter(user=user)
		cities = {}
		days = {}
		output = {}
		for trip in trips:
			#cities[trip] = VisitedCity.objects.filter(trip = trip)
			output[trip] = VisitedCity.objects.filter(trip = trip)
			for city in cities:
				ds = VisitedDay.objects.filter(visited_city=city)
				#days[city]=ds
				output[trip][city]=VisitedDay.objects.filter(visited_city=city)

	return render(request, 'viewpost.html', {'post' : post,'trips':trips,'cities':cities, 'output':output, 'post_id':id})