from audioop import maxpp
from re import T
from django.db import models

# Create your models here.
class Report(models.Model):
    """Report model."""
    SEX_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('O', 'Otro'),
    ]

    datetime = models.DateField()
    place = models.TextField()
    name = models.CharField(max_length=150, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEX_CHOICES, null=True, blank=True)
    edad = models.PositiveIntegerField(null=True, blank=True)
    ocupacion = models.CharField(max_length=150, null=True, blank=True)
    escolaridad_d = models.CharField(max_length=150, null=True, blank=True)
    name_d = models.CharField(max_length=150, null=True, blank=True)
    ocupacion_d = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to="users/denuncia/imagenes", blank=True, null=True)
    video = models.FileField(upload_to=u"users/denuncia/videos", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return str(self.ocupacion_d)
