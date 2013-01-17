from django.http import HttpResponse
import datetime

def viewtrip(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)