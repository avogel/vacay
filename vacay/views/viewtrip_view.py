from django.template.loader import get_template
from django.http import Http404
from vacay.vposts.models import *
from django.shortcuts import render

def viewtrip(request, id):
	try:
		id = int(id)
	except ValueError:
		raise Http404()
	trip = Trip.objects.get(id=id)
	user = request.user
	trips = Trip.objects.filter(user = user)
	cities = VisitedCity.objects.filter(trip=trip)
	days = {}
	for city in cities:
		ds = VisitedDay.objects.filter(visited_city=city)
		days[city]=ds
	return render(request, 'viewtrip.html', {'trips':trips,'trip' : trip,'cities' : cities, 'days':days})
