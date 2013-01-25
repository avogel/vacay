from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from vacay.vposts.models import Trip
from django.utils import simplejson
import json
from vacay.forms import TestForm

@login_required
def pasttrips(request):
	user = request.user
	if request.method == 'POST':
		print "got to pasttrips"
		form = TestForm(request.POST)
		num = "did not work"
		if form.is_valid():
			num = request.POST['num']
		print num
		return HttpResponse(simplejson.dumps({'num' : num, 'y': 1000}))

	past_trips = Trip.objects.filter(user=user, is_completed=True)
	return render(request, 'pasttrips.html', {'past_trips': past_trips})
