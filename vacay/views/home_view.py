from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from vacay.vposts.models import Trip
from vacay.vposts.models import Post
from django.db.models import Q

@login_required
def home(request):
	user = request.user
	trips = Trip.objects.filter(user=user)    	
	future_trips = Trip.objects.filter(user=user, is_completed=False)
	past_trips = Trip.objects.filter(user=user, is_completed=True)	 
	recommended = Post.objects.filter(Q(title__icontains='New York') | Q(contents__icontains='New York')| Q(contents__icontains='city')) 	
	recommended = recommended[:15]
	return render(request, 'home.html', {'trips':trips,'future_trips':future_trips,'past_trips': past_trips,'recommended':recommended})