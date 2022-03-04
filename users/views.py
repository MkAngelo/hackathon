from django.shortcuts import redirect, render
from users.forms import ReportForm
from users.models import Report

# Create your views here.
def home(request):
    """Home page"""
    return render(request, 'users/home.html')

def denuncia(request):
    """Denuncia page"""
    if request.method == 'POST':
        fecha = request.POST['fecha']
        nombre_den = request.POST['nombre_denunciado']
        ocupacion_den = request.POST['ocupacion_denunciado']
        lugar = request.POST['lugar']
        
        if fecha == "" or nombre_den == "" or ocupacion_den == "" or lugar == "":
            return render(request, 'users/denuncia.html', {'error': 'Necesitas llenar los campos que tienen un (*)'})
        report = Report.objects.create(
            datetime = fecha,
            place = lugar,
            name_d = nombre_den,
            ocupacion_d = ocupacion_den,
            name = request.POST['nombre_victima'],
            sexo = request.POST['sexo'],
            edad = request.POST['edad'],
            ocupacion = request.POST['ocupacion'],
            escolaridad_d = request.POST['escolaridad_denunciado'],
            descripcion = request.POST['descripcion'],
            imagen = request.POST['foto'],
            video = request.POST['video'],
            email = request.POST['email']
        )
        return redirect('users:home')

    return render(request, 'users/denuncia.html')