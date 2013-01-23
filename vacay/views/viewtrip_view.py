from django.template.loader import get_template
from django.http import Http404
from vacay.vposts.models import *
from django.shortcuts import render_to_response

def viewtrip(request, id):
	try:
		id = int(id)
	except ValueError:
		raise Http404()
	trip = Trip.objects.get(id=id)
	cities = VisitedCity.objects.filter(trip=trip)
	days = {}
	posts = {}
	for city in cities:
		ds = VisitedDay.objects.filter(visited_city=city)
		days[city]=ds
		for day in ds:
			posts[day] = day.written_posts 
	return render_to_response('viewtrip.html', {'trip' : trip,'cities' : cities, 'days':days, 'posts':posts})