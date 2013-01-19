from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def search(request):
    results = ["stuff", "stuff", "stuff"]
    t = get_template('search.html')
    html = t.render(Context({'results': results}))
    return HttpResponse(html)