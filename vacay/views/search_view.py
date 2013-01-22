from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from vacay.vposts.models import Post

def search(request, query):
	if query == "":
		results = ""
	else:
		user = request.user
		results = Post.objects.filter(Q(title__icontains=query) | Q(contents__icontains=query))
	return render_to_response('search.html', {'results': results})

def emptysearch(request):
    if 'query' in request.GET:
    	query = request.GET['query']
    	return HttpResponseRedirect(reverse('vacay.views.search_view.search', args=(query,)))
    else:
        return search(request,"")