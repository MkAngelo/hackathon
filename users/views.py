from django.shortcuts import redirect, render
from django.contrib import messages
from users.models import Report

# Create your views here.
def home(request):
    """Home page"""
    return render(request, 'users/home.html')

def denuncia(request):
    """Denuncia page"""
    if request.method == 'POST':
        fecha = request.POST['fecha']
        descri = request.POST['descripcion']
        nombre_den = request.POST['nombre_denunciado']
        ocupacion_den = request.POST['ocupacion_denunciado']
        lugar = request.POST['lugar']
        
        if fecha == "" or descri == "" or ocupacion_den == "" or lugar == "":
            return render(request, 'users/denuncia.html', {'error': 'Necesitas llenar los campos que tienen un (*)'})
        report = Report.objects.create(
            datetime = fecha,
            place = lugar,
            name_d = nombre_den,
            ocupacion_d = ocupacion_den,
            name = request.POST['nombre_victima'],
            sexo = request.POST['sexo'],
            ocupacion = request.POST['ocupacion'],
            escolaridad_d = request.POST['escolaridad_denunciado'],
            descripcion = descri,
            imagen = request.POST['foto'],
            video = request.POST['video'],
            email = request.POST['email'],
        )

        if(request.POST['edad'] == ""):
            report.edad = 0;
        else:
            report.edad = request.POST['edad']

        report.save()

        messages.success(request, "Recuerda que los trámites de gobierno puden ser tardados, así que no te desesperes, todo saldrá bien.")
        return redirect('users:denuncia')

    return render(request, 'users/denuncia.html')

def terminos(request):
    """Terminos y condiciones"""
    return render(request, "terminos.html")