from django.template.loader import get_template
from django.shortcuts import render
from django.http import Http404
import datetime
from django.contrib.auth.decorators import login_required
from vacay.vposts.models import Trip

@login_required
def futuretrips(request):
	user = request.user
	future_trips = Trip.objects.filter(user=user, is_completed=False)
	return render(request, 'futuretrips.html', {'future_trips': future_trips})