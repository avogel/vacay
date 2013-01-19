from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def futuretrips(request):
    future_trips = ["1","2"]
    t = get_template('futuretrips.html')
    html = t.render(Context({'future_trips': future_trips}))
    return HttpResponse(html)