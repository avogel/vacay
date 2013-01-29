from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from vacay.vposts.models import Trip

@login_required
def home(request):
	user = request.user	    	
	future_trips = Trip.objects.filter(user=user, is_completed=False)
	past_trips = Trip.objects.filter(user=user, is_completed=True)	  	
	return render(request, 'home.html', {'future_trips':future_trips,'past_trips': past_trips})