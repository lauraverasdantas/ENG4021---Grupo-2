from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def crise(request):
    return render(request, 'crise/crise.html')

