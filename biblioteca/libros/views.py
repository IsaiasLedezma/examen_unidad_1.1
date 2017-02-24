from django.shortcuts import render

# Create your views here.
def home123(request):
    m = "Hola biblioteca"
    contexto= {"mensaje":m}
    return render(request, 'home.html', contexto)
