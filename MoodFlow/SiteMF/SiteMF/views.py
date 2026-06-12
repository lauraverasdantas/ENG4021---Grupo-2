from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'SiteMF/home.html')