from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from vacay.vposts.models import Trip
import json
from vacay.forms import TestForm

@login_required
def pasttrips(request):
	user = request.user
	# if request.method == 'POST':
	# 	form = TestForm(request.POST)
	# 	num = "did not work"
	# 	if form.is_valid():
	# 		num = request.POST['num']
	# 	return HttpResponse(json.dumps({'num':num}))

	past_trips = Trip.objects.filter(user=user, is_completed=True)
	return render_to_response('pasttrips.html', {'past_trips': past_trips})
