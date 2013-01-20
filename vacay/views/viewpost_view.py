from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import render_to_response
from vacay.vposts.models import Post
import datetime

def viewpost(request, id):
	try:
		id = int(id)
		print id
	except ValueError:
		raise Http404()
	post = Post.objects.get(id=id)
	return render_to_response('viewpost.html', {'post' : post})