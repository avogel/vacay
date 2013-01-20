from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
from vacay.vposts.models import Trip

@login_required
def mytrips(request):
	user = request.user
	past_trips = Trip.objects.filter(user=user, is_completed=False)
	future_trips = Trip.objects.filter(user=user, is_completed=True)
	t = get_template('mytrips.html')
	html = t.render(Context({}))
	return HttpResponse(html)