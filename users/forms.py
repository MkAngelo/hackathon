"""User Forms"""

# Django
from django import forms

# Models
from users.models import Report

class ReportForm(forms.ModelForm):
    model = Report
    fields = (
        'datetime',
        'place',
        'name',
        'sexo',
        'edad',
        'ocupacion',
        'escolaridad_d',
        'name_d',
        'ocupacion_d',
        'descripcion',
        'imagen',
        'video',
        'email'
    )