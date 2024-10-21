# myapp/urls.py

from django.urls import path
from . import views  # Importa tus vistas

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('agregar_empleado/', views.agregar_empleado, name='agregar_empleado'),  # Ruta para agregar empleados
    path('crear_proyecto/', views.crear_proyecto, name='crear_proyecto'),  # Crear proyecto
    path('editar_proyectos/', views.editar_proyectos, name='editar_proyectos'),  # Listar proyectos
    path('crear-equipo/', views.crear_equipo, name='crear_equipo'),  # Nueva vista para crear equipo
    path('crear_tarea/<int:proyecto_id>/', views.crear_tarea, name='crear_tarea'),
    path('detalles_proyecto/<int:proyecto_id>/', views.detalles_proyecto, name='detalles_proyecto'),  # Nueva ruta
    path('editar_proyectos/', views.editar_proyectos, name='editar_proyectos'),  # Ruta para editar proyectos

    path('equipo/confirmar_eliminar/<int:equipo_id>/', views.confirmar_eliminar_equipo, name='confirmar_eliminar_equipo'),


    path('equipos/', views.listar_equipos, name='listar_equipos'),  # Ruta para listar equipos
    path('eliminar-equipo/<int:equipo_id>/', views.eliminar_equipo, name='eliminar_equipo'),  # Ruta para eliminar un equipo
]
