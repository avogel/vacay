from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    now = datetime.datetime.now()
    t = get_template('home.html')
    html = t.render(RequestContext(request, {'current_date': now}))
    return HttpResponse(html)