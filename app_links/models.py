from django.db.models.fields import DateTimeField
from django.db import models

class Enlace(models.Model):
    fecha_registro = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(max_length=150)
    enlace = models.TextField(max_length=50)

    def __str__(self) -> str:
        return f'El enlace es {self.enlace}'
    
