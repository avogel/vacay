from django.template.loader import get_template
from django.http import Http404, HttpResponseRedirect
from vacay.vposts.models import *
from django.shortcuts import render

def viewtrip(request, id):
	try:
		id = int(id)
	except ValueError:
		raise Http404()
	try:
		trip = Trip.objects.get(id=id)
	except Exception, e:
		return HttpResponseRedirect('/home/')
	user = request.user
	trips = Trip.objects.filter(user = user)
	return render(request, 'viewtrip.html', {'trips':trips,'trip' : trip})
