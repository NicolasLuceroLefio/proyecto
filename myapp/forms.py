# myapp/forms.py
from django.forms import DateInput 
from django import forms
from .models import Empleado
from .models import Proyecto

from django import forms
from .models import Equipo, Empleado
from .models import Tarea

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'correo', 'cargo']

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'equipo']


class EquipoForm(forms.ModelForm):
    miembros = forms.ModelMultipleChoiceField(
        queryset=Empleado.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Equipo
        fields = ['nombre', 'miembros']   


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['descripcion', 'responsable', 'ejecutor', 'estado', 'fecha_inicio', 'fecha_final']  # Agrega los nuevos campos

    fecha_inicio = forms.DateField(widget=DateInput(attrs={'type': 'date'}), label='Fecha de Inicio', required=True)
    fecha_final = forms.DateField(widget=DateInput(attrs={'type': 'date'}), label='Fecha Final', required=True)

    def __init__(self, *args, **kwargs):
        proyecto_id = kwargs.pop('proyecto_id', None)
        super(TareaForm, self).__init__(*args, **kwargs)
        
        if proyecto_id:
            proyecto = Proyecto.objects.get(id=proyecto_id)
            equipo = proyecto.equipo
            miembros_equipo = equipo.miembros.all()
            self.fields['responsable'].queryset = miembros_equipo
            self.fields['ejecutor'].queryset = miembros_equipo



           