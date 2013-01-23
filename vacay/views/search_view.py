from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.shortcuts import render
from vacay.vposts.models import Post

def search(request, query):
	if query == "":
		results = []
	else:
		user = request.user
		results = Post.objects.filter(Q(title__icontains=query) | Q(contents__icontains=query))
	return render(request, 'search.html', {'results': results})

def emptysearch(request):
    if 'query' not in request.GET:
    	return search(request, "")
    elif not request.GET['query'] == '':
    	query = request.GET['query']
    	return HttpResponseRedirect('/vacay/search/%s/' % query)
    else:
        return HttpResponseRedirect('/vacay/search/')