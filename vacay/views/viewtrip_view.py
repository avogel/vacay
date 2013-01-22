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
	for city in cities:
		days[city] = VisitedDay.objects.filter(visited_city=city)
	print days
	return render_to_response('viewtrip.html', {'trip' : trip,'cities' : cities, 'days':days})