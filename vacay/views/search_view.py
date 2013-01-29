from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.shortcuts import render
from vacay.vposts.models import Post

def search(request):
	if 'query' not in request.GET or request.GET['query'] == "":
		query = ""
		results = []
	else:
		query = request.GET['query']
		user = request.user
		results = Post.objects.filter(Q(title__icontains=query) | Q(contents__icontains=query))
	return render(request, 'search.html', {'results': results, 'query': query})