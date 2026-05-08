from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Estudiante, Carrera
from .forms import EstudianteForm, CarreraForm
# Create your views here.

class lista(ListView):
    template_name = 'mi_aplicacion/lista.html'
    queryset = ['elemento 1', 'elemento2' ]
    context_object_name = 'lista'

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'mi_aplicacion/lista_estudiantes.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'mi_aplicacion/detalle_estudiante.html', {'estudiante': estudiante})

def crear_estudiante(request):
    if request.method == 'POST':
        estudiante_form = EstudianteForm(request.POST, request.FILES)
        if estudiante_form.is_valid():
            # Guardar el nuevo estudiante en la base de datos
            estudiante_form.save()
            return redirect('lista_estudiantes')  # Redirigir a la lista de estudiantes después de guardar
    else:
        estudiante_form = EstudianteForm()

    return render(request, 'mi_aplicacion/crear_estudiante.html', {'estudiante_form': estudiante_form})

def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES, instance=estudiante)

        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')  # Redirigir al detalle del estudiante después de guardar
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'mi_aplicacion/editar_estudiante.html', {'form': form})

def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista_estudiantes')  # Redirigir a la lista de estudiantes después de eliminar
    return render(request, 'mi_aplicacion/eliminar_estudiante.html', {'estudiante': estudiante})

def  crear_carrera(request):
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            # Guardar la nueva carrera en la base de datos
            form.save()
            return redirect('lista_carreras')  # Redirigir a la lista de estudiantes después de guardar
    else:
        form = CarreraForm()
    return render(request, 'mi_aplicacion/crear_carrera.html', {'form': form})

#Lista de carreras
def lista_carreras(request):
    carreras = Carrera.objects.all()
    return render(request, 'mi_aplicacion/lista_carreras.html', {'carreras': carreras})

def editar_carrera(request, pk):
    carrera = get_object_or_404(Carrera, pk=pk)
    if request.method == 'POST':
        form = CarreraForm(request.POST, instance=carrera)

        if form.is_valid():
            form.save()
            return redirect('lista_carreras')  # Redirigir al detalle del estudiante después de guardar
    else:
        form = CarreraForm(instance=carrera)
    return render(request, 'mi_aplicacion/editar_carrera.html', {'form': form})

def eliminar_carrera(request, pk):
    carrera = get_object_or_404(Carrera, pk=pk)
    if request.method == 'POST':
        carrera.delete()
        return redirect('lista_carreras')  # Redirigir a la lista de carreras después de eliminar
    return render(request, 'mi_aplicacion/eliminar_carrera.html', {'carrera': carrera})

def detalle_carrera(request, pk):
    carrera = get_object_or_404(Carrera, pk=pk)
    return render(request, 'mi_aplicacion/detalle_carrera.html', {'carrera': carrera})