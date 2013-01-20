from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def mytrips(request):
    now = datetime.datetime.now()
    return render_to_response('mytrips.html', {'current_date': now})