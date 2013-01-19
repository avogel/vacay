from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from vacay.vposts.models import Post
import datetime

def viewpost(request):
    post = Post.objects.all()[0]
    t = get_template('viewpost.html')
    html = t.render(Context({'post': post}))
    return HttpResponse(html)