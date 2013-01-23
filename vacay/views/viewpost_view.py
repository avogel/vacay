from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import render
from vacay.vposts.models import Post
import datetime

def viewpost(request, id):
	try:
		id = int(id)
		print id
	except ValueError:
		raise Http404()
	post = Post.objects.get(id=id)
	return render(request, 'viewpost.html', {'post' : post})