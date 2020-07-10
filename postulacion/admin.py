from django.contrib import admin
from .models import (Ciudad,
                     Comuna,
                     Region,
                     Postulante)


# Register your models here.

class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombres', 'apellidos', 'rut', 'vigente')
    fields = ('nombres',
              'apellidos',
              'email',
              'rut',
              'telefono',
              'direccion',
              'comuna',
              'vigente',
              )


admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Postulante, PostulanteAdmin)
