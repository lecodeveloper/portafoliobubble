from django.db import models

class personas_de_contacto(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField()
    tel = models.CharField(max_length=10 , blank= True)
    cuantos_ninos = models.IntegerField()
    edad_ninos = models.CharField(max_length=120)
    dias = models.CharField(max_length=120)
    horas_semana = models.IntegerField()
    opciones_aplican1 = models.BooleanField(verbose_name="Clases de inglés con anterioridad.")
    opciones_aplican2 = models.BooleanField(verbose_name="Grado preescolar y ha estado en escuela.")


    opciones = [
        ('Email', 'Email'),
        ('Tel', 'Teléfono'),
        ('Ambos', 'Ambos')
    ]
    metodo_comunicacion= models.CharField(max_length=15, choices=opciones)

    def __str__(self):  #esta función hace que se guarde en la base de datos de django con el nombre en lugar de object1 etc.
        return self.nombre