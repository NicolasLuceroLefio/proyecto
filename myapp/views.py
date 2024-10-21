
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm  # Asegúrate de tener un formulario para los empleados
from .forms import ProyectoForm
from .models import Equipo
from .forms import EquipoForm
from .models import Proyecto

from.models import Tarea  # Asegúrate de tener una tabla de tareas en su modelo
from .forms import TareaForm

from django.urls import reverse

def index(request):
    # Esta vista solo muestra la página principal
    return render(request, 'myapp/index.html')

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_empleado')  # Redirige a la misma vista después de guardar
    else:
        form = EmpleadoForm()
    
    empleados = Empleado.objects.all()  # Obtiene todos los empleados para listarlos
    return render(request, 'myapp/agregar_empleado.html', {'form': form, 'empleados': empleados})


def index(request):
    empleados = Empleado.objects.all()  # Esto es para la lista de empleados
    return render(request, 'myapp/index.html', {'empleados': empleados})


def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proyectos')  # Redirigir a la página principal después de guardar
    else:
        form = ProyectoForm()
    return render(request, 'crear_proyecto.html', {'form': form})

def editar_proyectos(request):
    proyectos = Proyecto.objects.all()  # Obtiene todos los proyectos para listarlos

    if request.method == 'POST':
        # Aquí puedes manejar la lógica para editar el proyecto si es necesario
        proyecto_id = request.POST.get('proyecto_seleccionado')
        if proyecto_id:
            return redirect('crear_tarea', proyecto_id=proyecto_id)  # Redirigir a la vista de detalles

    return render(request, 'editar_proyectos.html', {'proyectos': proyectos})



def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a la página de equipos
    else:
        form = EquipoForm()

    return render(request, 'crear_equipo.html', {'form': form})


def crear_tarea(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == 'POST':
        form = TareaForm(request.POST, proyecto_id=proyecto_id)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.proyecto = proyecto
            tarea.save()
            return redirect('editar_proyectos')
    else:
        form = TareaForm(proyecto_id=proyecto_id)

    return render(request, 'crear_tarea.html', {'form': form, 'proyecto': proyecto})

def detalles_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    tareas = proyecto.tareas.all()  # Obtener las tareas relacionadas con el proyecto
    equipo = proyecto.equipo  # Obtener el equipo relacionado con el proyecto
    return render(request, 'detalles_proyecto.html', {'proyecto': proyecto, 'tareas': tareas, 'equipo': equipo})



def eliminar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    equipo.delete()  # Esto eliminará en cascada los proyectos y tareas asociados
    return redirect(reverse('listar_equipos'))  # Redirige a una página después de eliminar

def confirmar_eliminar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)

    if request.method == "POST":
        equipo.delete()
        return redirect('lista_equipos')  # Redirige a la lista de equipos después de eliminar

    return render(request, 'confirmar_eliminar_equipo.html', {'equipo': equipo})

def listar_equipos(request):
    equipos = Equipo.objects.all()  # Recupera todos los equipos de la base de datos
    return render(request, 'listar_equipos.html', {'equipos': equipos})  # Pasa los equipos a la plantilla