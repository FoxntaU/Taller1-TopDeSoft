from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse
from django import forms
from .models import Archivo
from django.views.generic.base import View
import os
from django.conf import settings
from django.contrib import messages

class DetalleArchivoView(TemplateView):
    template_name = 'pages/detail.html'

    def get(self, request, archivo_id):
        archivo = Archivo.objects.get(id=archivo_id)
        return render(request, self.template_name, {'archivo': archivo})
    
class EliminarArchivoView(View):
    def post(self, request, pk):
        archivo = Archivo.objects.get(id=pk)
        # Eliminar el archivo físico del sistema de archivos
        if archivo.archivo:
            file_path = os.path.join(settings.MEDIA_ROOT, str(archivo.archivo))
            if os.path.exists(file_path):
                os.remove(file_path)
        # Eliminar el objeto Archivo de la base de datos
        archivo.delete()
        return HttpResponseRedirect(reverse('data'))


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class Data(TemplateView):
    template_name = 'pages/data.html'
    def get(self, request):
        archivos = Archivo.objects.all()
        return render(request, self.template_name, {'archivos': archivos})


class ArchivoForm(forms.Form):
    # this is for 1 file 
    nombre = forms.CharField(max_length=100)
    file = forms.FileField()
    # file = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class UploadFileView(View):
    template_name = 'pages/createdata.html'

    def get(self, request):
        form = ArchivoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            archivo = form.cleaned_data['file']
            archivo_obj = Archivo.objects.create(nombre=nombre, archivo=archivo)
            if archivo_obj:
                messages.success(request, 'Archivo creado exitosamente.')
            else:
                messages.error(request, 'Error al crear el archivo.')
        return render(request, self.template_name, {'form': form})
