from django.shortcuts import render

from models import libro

# Create your views here.
def home123(request):
    m = "Hola biblioteca"
    contexto = {"mensaje":m}
    return render(request, 'home.html', contexto)


def lista_libros(request):
    libros = libro.objects.all()
    print request
    i= "Libros nuevos"
    template = "listaDeLibros.html"
    context  = {"mensaje": i, "libro": libros}
    return render(request, template, context)
