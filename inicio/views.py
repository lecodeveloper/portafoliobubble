from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import RawPersonasForm

from .models import personas_de_contacto

# Create your views here.
def inicio(request):
    my_form = RawPersonasForm() #Declaración de variable con un método GET porque el POST se hará al dar click en enviar,
                                # si no validamos, dará error en el contexto
    if request.method == "POST":
        my_form = RawPersonasForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data) #este print solo lo hacemos para obersvar la información que se mandará viene en diccionario.
            personas_de_contacto.objects.create(**my_form.cleaned_data) #Con este comando ahora si estamos creando un objeto con esa información.
                                                                #El doble asterisco significa que pasaremos argumentos en lugar de diccionarios.
            return HttpResponseRedirect("/gracias")
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }

    return render(request, "inicio/form2.html", context)

def acerca(request):
    return render(request, "inicio/acerca.html")

def servicios(request):
    return render(request, "inicio/servicios.html")

def calendario(request):
    return render(request, "inicio/calendario.html")

def gracias(request):
    return render(request, "inicio/gracias.html")

def portafolio(request):
    return render(request, "inicio/portafolio.html")



#para forms ejemplo

'''def formEjemplo(request):
    form = personasForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form' : form
    }

    return render(request, "inicio/crear.html", context)'''

'''def formEjemplo2(request):

    if request.method == "POST":
        nuevo_nombre = request.POST.get('name')
        print(nuevo_nombre)
        #personas_de_contacto.objects.create(nombre=nuevo_nombre, ...etc)
    

    context = {}
    return render(request, "inicio/crear.html", context)'''

def formEjemplo3(request):
    my_form = RawPersonasForm() #Declaración de variable con un método GET porque el POST se hará al dar click en enviar,
                                # si no validamos, dará error en el contexto
    if request.method == "POST":
        my_form = RawPersonasForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data) #este print solo lo hacemos para obersvar la información que se mandará viene en diccionario.
            personas_de_contacto.objects.create(**my_form.cleaned_data) #Con este comando ahora si estamos creando un objeto con esa información.
                                                                #El doble asterisco significa que pasaremos argumentos en lugar de diccionarios.
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }

    return render(request, "inicio/form2.html", context)


