from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def mytrips(request):
    now = datetime.datetime.now()
    t = get_template('mytrips.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)