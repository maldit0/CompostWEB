from django.core.validators import RegexValidator
from django.db import models


class Region(models.Model):
    valor = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Regiones'

    def __str__(self):
        return "{0}".format(self.valor)


class Ciudad(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    valor = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return "{0}".format(self.valor)


class Comuna(models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    valor = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Comunas'

    def __str__(self):
        return "{0}".format(self.valor)


class Postulante(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    rut = models.CharField(max_length=20, validators=[
        RegexValidator('^\d{1,2}\.?\d{3}\.?\d{3}[-]?[0-9kK]{1}$', message='Ingrese un RUT Valido')])
    email = models.EmailField(max_length=50)
    telefono = models.BigIntegerField()
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, blank=True)
    direccion = models.CharField(max_length=75)
    vigente = models.BooleanField(default=True)
    f_postulacion = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Postulantes'

    def __str__(self):
        return f'\nNombre: {self.nombres} {self.apellidos} \nRUT: {self.rut}'
