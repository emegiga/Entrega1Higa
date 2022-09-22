from django.shortcuts import render
from django.http import HttpResponse
from BlogBuster.models import Vhs, Cds, Videojuegos
from BlogBuster.forms import *

# Create your views here.

#Vista de inicio
def inicio(request):
    return render(request, "BlogBuster/inicio.html")

# Agrega el registro a la tabla VHS
def inputVhs(request):
    if request.method == "POST":
        form1 = FormVHS(request.POST)
        if form1.is_valid():
            info = form1.cleaned_data
            vhs = Vhs(titulo=info["titulo"], genero=info["genero"], anioLanzamiento=info["anioLanzamiento"], director=info["director"])
            vhs.save()
            return render(request, "BlogBuster/inicio.html")
    else:
        form1=FormVHS()
    ##Código de prueba (ingreso manual de datos a la BD)##
    #item1 = Vhs(titulo="Porco Rosso", genero="Anime", anioLanzamiento=1992, director="Studio Ghibli")
    #item1.save()
    #return HttpResponse(f"Has registrado el título {item1.titulo}. Su género es {item1.genero}.")
    return render(request, "BlogBuster/cargardatosvhs.html", {"form1":form1})

# Agrega el registro a la tabla CDs
def inputCds(request):
    if request.method == "POST":
        form2 = FormCds(request.POST)
        if form2.is_valid():
            info = form2.cleaned_data
            cds = Cds(nombre=info["nombre"], artista=info["artista"], anioLanzamiento=info["anioLanzamiento"], genero=info["genero"])
            cds.save()
            return render(request, "BlogBuster/inicio.html")
    else:
        form2=FormCds()
    ##Código de prueba (ingreso manual de datos a la BD)##
    #item2 = Cds(nombre="Exodus", artista="Bob Marley and The Wailers", anioLanzamiento=1977, genero="Reggae")
    #item2.save()
    #return HttpResponse(f"Has registrado el título {item2.nombre} del artista {item2.artista}. Su género es {item2.genero}.")
    return render(request, "BlogBuster/cargardatoscds.html")

# Agrega el registro a la tabla Videojuegos
def inputVideojuegos(request):
    if request.method == "POST":
        form3 = FormJuegos(request.POST)
        if form3.is_valid():
            info = form3.cleaned_data
            juegos = Videojuegos(nombre=info["nombre"], desarrolladora=info["desarrolladora"], plataforma=info["plataforma"], genero=info["genero"])
            juegos.save()
            return render(request, "BlogBuster/inicio.html")
    else:
        form3=FormJuegos()
    ##Código de prueba (ingreso manual de datos a la BD)##
    #item3 = Videojuegos(nombre="Star Wars Jedi Knight: Jedi Academy", desarrolladora="LucasArts", plataforma="PC", genero="Adventure")
    #item3.save()
    #return HttpResponse(f"Has registrado el título {item3.nombre} de la desarrolladora {item3.desarrolladora}. Su género es {item3.genero}.")
    return render(request, "BlogBuster/cargardatosvideojuegos.html")

# Buscador VHS
def searchVhs(request):
    return render(request, "BlogBuster/buscarVhs.html")

# Resultados VHS 
def resultadoVhs(request):
    if request.GET["titulo"]:
        busqueda = request.GET["titulo"]
        vhs = Vhs.objects.filter(titulo__iexact=busqueda)
        return render(request, "BlogBuster/resultadosVhs.html", {"vhs":vhs, "busqueda":busqueda})
    else:
        mensaje = "No enviaste datos."
    return render(mensaje)    