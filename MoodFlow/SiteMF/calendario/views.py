from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def calendario(request):
    return render(request, 'calendario/calendario.html')
