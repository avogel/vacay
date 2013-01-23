from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from vacay.vposts.models import Trip
	  	
@login_required	  	
def mytrips(request):	  	
  user = request.user	  	
  #past_trips = Trip.objects.filter(user=user, is_completed=False)	  	
  #future_trips = Trip.objects.filter(user=user, is_completed=True)	  	
  return render(request, 'mytrips.html', {})