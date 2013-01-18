from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def viewpost(request):
    now = datetime.datetime.now()
    t = get_template('viewpost.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)