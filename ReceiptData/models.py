from django.db import models

class Archivo(models.Model):
    nombre = models.CharField(max_length=100, default='none')
    archivo = models.FileField()
    fecha_subida = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.archivo.nombre
