from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import render_to_response
import datetime
from django.contrib.auth.decorators import login_required
from vacay.vposts.models import Trip

@login_required
def pasttrips(request):
	user = request.user
	past_trips = Trip.objects.filter(user=user, is_completed=False)
	return render_to_response('pasttrips.html', {'past_trips': past_trips})