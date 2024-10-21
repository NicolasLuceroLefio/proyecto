from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    miembros = models.ManyToManyField(Empleado)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)  # Eliminación en cascada

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha_inicio = models.DateField(null=True)
    fecha_final = models.DateField(null=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')  # Eliminación en cascada
    responsable = models.ForeignKey(Empleado, related_name='responsable_tareas', on_delete=models.CASCADE)
    ejecutor = models.ForeignKey(Empleado, related_name='ejecutor_tareas', on_delete=models.CASCADE)
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada', 'Completada'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return self.descripcion
