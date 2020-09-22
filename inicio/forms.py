from django import forms

from .models import personas_de_contacto

#class personasForm(forms.ModelForm):
#    class Meta:
#        model = personas_de_contacto
#        fields = [
#            'nombre',
#            'tel',
#            'cuantos_ninos',
#        ]

class RawPersonasForm(forms.Form):
    nombre         = forms.CharField(label="Nómbre*")
    email           = forms.EmailField(label="Email*")
    tel            = forms.CharField(label="Teléfono", required=False, empty_value= "No proporcionado")
    cuantos_ninos   = forms.IntegerField(label="Número de niños con interés*")
    edad_ninos      = forms.CharField(label="Edad(es)*")
    dias             = forms.CharField(label="Días preferibles", required=False, empty_value="No proporcionado")
    horas_semana     = forms.IntegerField(label="¿Cuántas horas a la semana?*")
    
    
    opciones = [
        ('Email', 'Email'),
        ('Tel', 'Teléfono'),
        ('Ambos', 'Ambos')
    ]
    opciones_aplican1 = forms.BooleanField(label="El(los) alumnos han estado en clases de inglés con anterioridad.", required=False,
    widget=forms.CheckboxInput(
        attrs={
            "class":"inputclass2",
            "id":"aplican1",
        }),
    )
    opciones_aplican2 = forms.BooleanField(label="El alumno es de grado preescolar y ha estado o está en escuela.", required=False,
    widget=forms.CheckboxInput(
        attrs={
            "class":"inputclass2",
            "id":"aplican1",
        }))
    
    metodo_comunicacion= forms.CharField(label="Seleccione un método de comunicación", widget=forms.Select(choices=opciones))