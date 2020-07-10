from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from .forms import PostulanteForm
from .models import Postulante, Comuna
from django.utils import timezone


# Create your views here.

class PostulanteCreateView(CreateView):
    form_class = PostulanteForm
    template_name = 'postulacion/postulacion.html'

    def get_success_url(self):
        return reverse('home', kwargs={})


class PostulanteListView(ListView):
    model = Postulante
    queryset = Postulante.objects.filter(vigente=True)
    template_name = 'postulacion/lista_postulaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PostulanteDetailView(DetailView):
    queryset = Postulante.objects.all()
    template_name = 'postulacion/detalle_postulacion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PostulanteUpdateView(UpdateView):
    form_class = PostulanteForm
    queryset = Postulante.objects.all()
    template_name = 'postulacion/modificar_postulacion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_success_url(self):
        return reverse('postulacion:lista_postulacion', kwargs={})


class PostulanteDeleteView(DeleteView):

    # from_class = PostulanteForm
    queryset = Postulante.objects.all()
    template_name = 'postulacion/eliminar_postulacion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_success_url(self):
        return reverse('postulacion:lista_postulacion', kwargs={})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        # cambiar estado
        self.object.vigente = False
        self.object.save()
        return HttpResponseRedirect(success_url)


