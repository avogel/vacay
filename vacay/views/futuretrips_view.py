from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import Http404
import datetime
from django.contrib.auth.decorators import login_required
from vacay.vposts.models import Trip

@login_required
def futuretrips(request):
	user = request.user
	future_trips = Trip.objects.filter(user=user, is_completed=True)
	return render_to_response('futuretrips.html', {'future_trips': future_trips})