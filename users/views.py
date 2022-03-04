from django.shortcuts import render
from users.forms import ReportForm

# Create your views here.
def home(request):
    """Home page"""
    return render(request, 'users/home.html')

def denuncia(request):
    """Denuncia page"""
    if request.method == 'POST':
        print('*'*10)
        datetime = request.POST['fecha']
        nombre_v = request.POST['nombre_victima']
        nombre_den = request.POST['nombre_denunciado']
        print(nombre_v,nombre_den, datetime)
        print('*'*10)
    return render(request, 'users/denuncia.html')