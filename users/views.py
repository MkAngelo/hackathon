from django.shortcuts import render

# Create your views here.
def home(request):
    """Home page"""
    return render(request, 'users/home.html')

def denuncia(request):
    """Denuncia page"""
    return render(request, 'users/denuncia.html')