from django.urls import path
from . import views

urlpatterns = [
    path('',views.saludo2),
    path('consulta/',views.Consulta),
    path('hello /<str:username>', views.hello),
    path('Projectos/', views.projects),
    path('task/<int:id>', views.tasks),
    path('index/',views.Index),
    path('about/',views.About),
    path('Proyectos/',views.Proyectos),
    path('Tareas/',views.Task),
    path('CraerTarea/',views.Create_Task)
]