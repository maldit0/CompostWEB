from django.urls import path
from . import views

app_name = 'postulacion'

urlpatterns = [
    path('', views.PostulanteCreateView.as_view(), name='postulacion'),
    path('lista_postulantes', views.PostulanteListView.as_view(), name='lista_postulacion'),
    path('detalle_postulacion/<int:pk>', views.PostulanteDetailView.as_view(), name='detalle_postulacion'),
    path('modificar_postulacion/<int:pk>', views.PostulanteUpdateView.as_view(), name='modificar_postulacion'),
    path('eliminar_postulacion/<int:pk>', views.PostulanteDeleteView.as_view(), name='eliminar_postulacion'),
    # path('lista_postulantes/<int:pk>', views.PostulanteDeleteView.as_view(), name='eliminar_postulacion'),
]
