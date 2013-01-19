from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def blogging(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)