from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def pasttrips(request):
    past_trips = ["test","testing"]
    t = get_template('pasttrips.html')
    html = t.render(Context({'past_trips': past_trips}))
    return HttpResponse(html)