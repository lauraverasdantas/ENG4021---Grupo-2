from django.shortcuts import render

def humor(request):
   
    return render(request, 'humor/humor.html')

