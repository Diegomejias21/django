from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('crud', views.crud, name="crud"),
    path('alumnos_add', views.alumnos_add, name="alumnos_add"),
    path('alumnos_edit', views.alumnos_edit, name="alumnos_edit"),
    #path('alumnos_list', views.alumnos_list, name="alumnos_list"),
    
    
    
    #path('listadoSQL', views.listadoSQL, name='listadoSQL')
]