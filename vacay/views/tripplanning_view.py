from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def tripplanning(request):
    return render(request, 'tripplanning.html', {})