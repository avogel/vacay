from django.template.loader import get_template
from django.http import Http404
from vacay.vposts.models import Trip
from django.shortcuts import render_to_response

def viewtrip(request, id):
	try:
		id = int(id)
	except ValueError:
		raise Http404()
	trip = Trip.objects.get(id=id)
	return render_to_response('viewtrip.html', {'trip' : trip})