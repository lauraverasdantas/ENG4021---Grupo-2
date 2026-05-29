from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def humor(request):
    return render(request, 'humor/humor.html')
