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
			if not trip.ideas.contains(post):
				trip.ideas.add(post)
		elif type == 'city':
			city = VisitedCity.objects.get(id=bookmark_id)
			if not city.ideas.contains(post):
				city.ideas.add(post)
		else:
			day = VisitedDay.objects.get(id=bookmark_id)
			if not day.ideas.contains(post):
				day.ideas.add(post)
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

	return render(request, 'viewpost.html', {'post' : post,'trips':trips,'cities':cities, 'output':output})