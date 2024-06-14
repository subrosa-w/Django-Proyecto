from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'gatos/index.html', context)

def formulario(request):
    context={}
    return render(request, 'gatos/formulario.html',context)

def login(request):
    context={}
    return render(request, 'gatos/login.html',context)

def seccion_perros(request):
    context={}
    return render(request, 'gatos/seccion_perros.html', context)

def seccion_gatos(request):
    context={}
    return render(request, 'gatos/seccion_gatos.html', context)

def gato1(request):
    context={}
    return render(request, 'gatos/gato1.html', context)

def gato2(request):
    context={}
    return render(request, 'gatos/gato2.html', context)

def gato3(request):
    context={}
    return render(request, 'gatos/gato3.html', context)

def perro1(request):
    context={}
    return render(request, 'gatos/perro1.html', context)

def perro2(request):
    context={}
    return render(request, 'gatos/perro2.html', context)

def perro3(request):
    context={}
    return render(request, 'gatos/perro3.html', context)