from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import Http404
from vacay.vposts.models import *
from django.db.models import Q

@login_required
def tripplanning(request, id):
	if 'query' not in request.GET or request.GET['query'] == '':
		q = ''
		results= []
	else:
		q = request.GET['query']
		results = Post.objects.filter(Q(title__icontains=q) | Q(contents__icontains=q))
	try:
		id = int(id)
	except ValueError:
		raise Http404()
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
		current_trip = Trip.objects.get(id=id)
		trips = Trip.objects.filter(user=user)
		cities = VisitedCity.objects.filter(trip=current_trip)
		days = {}
		#populates days for use in sidebar
		for city in cities:
			ds = VisitedDay.objects.filter(visited_city=city)
			days[city]=ds
	
	return render(request, 'tripplanning.html', { 'trips':trips, 'id':id, 'current_trip' : current_trip, 'days':days,'results':results,'q':q})
