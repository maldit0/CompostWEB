from django.urls import path
from . import views

app_name = 'usuarios'


urlpatterns = [

    path('', views.module_list, name='lista_modulos')
]