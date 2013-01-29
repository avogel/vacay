from django.shortcuts import render
from django.template import Context
from django.http import HttpResponseRedirect
from vacay.vposts.models import *
from vacay.forms import NewTripForm
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required

@login_required
def newtrip(request):
	user = request.user
	print "got here"
	city_list = get_cities_from_request(request)
	if request.method == 'POST':
		form = NewTripForm(request.POST, city_list=city_list)
		print "new trip form: ", form.data
		if form.is_valid():
			make_trip(user, city_list, form)
			return HttpResponseRedirect('/tripplanning/%d/' % 1)
	else:
		form = NewTripForm()
	print city_list
	return render(request, 'newtrip.html', {'form': form, 'city_list' : city_list})

def get_cities_from_request(request):
	city_list = []
	i = 1
	while ('city_name' + str(i)) in request.POST:
		city_name = request.POST['city_name' + str(i)]
		num_days = request.POST['num_days' + str(i)]
		try:
			num_days_int = int(num_days)
		except ValueError:
			num_days = ""
		if 'overlap' + str(i) in request.POST:
			overlap = request.POST['overlap' + str(i)]
		else:
			overlap = False
		city_list.append((city_name, num_days, overlap))
		i += 1
	return city_list

def make_trip(user, city_list, form):
	cd = form.cleaned_data
	trip = Trip(name=cd['name'], description=cd['description'], user=user, is_completed=False)
	trip.save()
	start_date = cd['start_date']
	day_num = 1
	for i, (city_name, num_days, overlap) in enumerate(city_list):
		visited_city = VisitedCity(city_name=city_name, city_number=i+1, trip=trip)
		visited_city.save()
		for i in range(int(num_days)):
			if start_date == None:
				visited_day = VisitedDay(day_number=day_num, visited_city=visited_city)
				visited_day.save()
			else:
				visited_day = VisitedDay(date=start_date+timedelta(days=day_num-1), day_number=day_num, visited_city=visited_city)
				visited_day.save()
			if not (i == int(num_days)-1 and overlap):
				day_num += 1