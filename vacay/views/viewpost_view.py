from django.template.loader import get_template
from django.http import Http404, HttpResponse, HttpResponseRedirect
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
	try:
		post = Post.objects.get(id=id)
	except Exception, e:
		return HttpResponseRedirect('/home/')
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

	return render(request, 'viewpost.html', {'post' : post,'trips':trips, 'post_id':id})