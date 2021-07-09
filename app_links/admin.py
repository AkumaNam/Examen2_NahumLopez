from django.contrib import admin
from django.contrib.admin.decorators import register
from app_links.models import Enlace
# Register your models here.

class EnlaceAdmin(admin.ModelAdmin):
    list_display = ('fecha_registro', 'descripcion', 'enlace')
    list_editable = ('descripcion', )
#----------------------------------------------------------------------------------------------
admin.site.register(Enlace, EnlaceAdmin)