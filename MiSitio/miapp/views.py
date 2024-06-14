from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .forms import CreateNewTask

from . import models

# Create your views here.


def saludo (request):
    return HttpResponse("Hola Mundo")

def saludo2 (request):
    return HttpResponse("<h1 style='text-align:center'>Hola Esta es la ruta Home🏡🏠</h1>")

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

def Task(request):
    tasks = models.Task.objects.all()                                                      
    return render(request,'tasks/tasks.html', {'tasks':tasks})

def Create_Task (request): 
    title = request.GET.get('title') 
    description = request.GET.get('description')      
    project = models.project.objects.get(id=1)      

    print(title)                                 
    print(description)                                 
    print(project)   

    if not(title is None or description is None):
        models.Task.objects.create(title=title,description=description, project=project)
        print('Entre')

    return render(request,'tasks/Create_Task.html', {'form': CreateNewTask()})
