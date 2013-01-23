from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def blogging(request):
    return render(request, 'blogging.html', {})