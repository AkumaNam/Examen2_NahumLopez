from django.shortcuts import render
from .models import Enlace

# Create your views here.
def index(request):
     return render(request, 'links/index.html')



def enlace(request): 

    if request.method == 'POST':
        fecha_registro = request.POST.get('fecha_registro')
        descripcion = request.POST.get('descripcion')
        enlace = request.POST.get('enlace')

        e = Enlace(fecha_registro = fecha_registro, descripcion = descripcion, enlace = enlace)
        e.save()

        msj = f''


    q = request.GET.get('q')

    if q:
        data = Enlace.objects.filter(fecha_registro__startswith = q).order_by('fecha_registro')

    else:
        data = Enlace.objects.all().order_by('fecha_registro')
    ctx = {
          'enlace': data,
          'q' : q,
    }
          
    return render(request, 'links/links.html', ctx)
