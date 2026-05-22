from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def listarusuario(request):
   
    return render(request, 'listarusuario/listarusuario.html')
