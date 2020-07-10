from .models import Postulante
from django import forms

class PostulanteForm(forms.ModelForm):
    class Meta:
        model = Postulante
        fields = ['nombres',
                  'apellidos',
                  'email',
                  'rut',
                  'telefono',
                  'direccion',
                  'comuna',
                  ]
