from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

from . import models

# Create your views here.


def saludo (request):
    return HttpResponse("Hola Mundo")

def saludo2 (request):
    return HttpResponse("Hola Mundo 2")

# def consulta
def Consulta(request):
    tareas = models.Task.objects.all()
    for i in tareas:
        print(f'Titulo: {i.title} FK: {i.project.name}')
    return  HttpResponse("Consulta")

def hello (request, username):
    print(username)
    return HttpResponse('<h1> %s</h1>'% username)
    # return HttpResponse('Hola Como vas'% username %'?')

def projects (request):
    projects = list(models.project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks (request, id):
    task = get_object_or_404(models.Task, id=id)
    return HttpResponse('task: %s'% task.title)

def Index(request):
    title='Bienvenido a Django'
    superusuarios = User.objects.filter(is_superuser=True)

    superusuarios_admin = listar_superusuarios_admin()
    for superusuario in superusuarios_admin:
        print(superusuario.username)

    return render(request,'index.html', {'title': title, 'SuperUsusarios':superusuarios})
def About(request):
    datos = { 'Nombre':"Juan", 'anio': 2000}
    return render(request,'About.html', {'datos':datos})
                     
def listar_superusuarios_admin():
    superusuarios = User.objects.filter(is_superuser=True)
    return superusuarios

def Proyectos(request):
    projects = models.project.objects.all()
    return render(request,'projects/projects.html', {'Proyectos':projects})

