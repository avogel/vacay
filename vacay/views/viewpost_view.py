from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import render
from vacay.vposts.models import *
import datetime

def viewpost(request, id):
	try:
		id = int(id)
		print id
	except ValueError:
		raise Http404()
	post = Post.objects.get(id=id)
	user = request.user
	if user.is_authenticated():
		trips = Trip.objects.filter(user=user)
		cities = {}
		days = {}
		output = {}
		for trip in trips:
			cities[trip] = VisitedCity.objects.filter(trip = trip)
			for city in cities:
				ds = VisitedDay.objects.filter(visited_city=city)
				days[city]=ds
	return render(request, 'viewpost.html', {'post' : post,'trips':trips,'cities':cities, 'days':days})