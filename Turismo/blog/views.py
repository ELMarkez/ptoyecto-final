from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Evento, Autor, Comentario


def inicio(request):    
    inicio = inicio.object.order_by("inicio")
    return render(request, "/home.html", {"inicio": inicio})


def crear_evento(request):
    eventos = Evento.objects.order_by("fecha_creacion")[:5]
    return render(request, "vistas/crear_evento.html", {"eventos": eventos})


def eventos(request):
    lista = Evento.objects.order_by("fecha_creacion")
    return render(request, "vistas/eventos.html", {"eventos": lista})


def detalle_evento(request, id):
    evento = Evento.objects.get(id=id)
    return render(request, "vistas/detalle_evento.html", {"evento": evento})


def login_usuario(request):
    if request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("password")
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return redirect("home")
    return render(request, "vistas/login.html")


def logout_usuario(request):
    logout(request)
    return redirect("home")


def registro(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "vistas/register.html", {"form": form})


@login_required
def crear_evento(request):
    if request.method == "POST":
        Evento.objects.create(
            autor_post=Autor.objects.get(user=request.user),
            titulo=request.POST["titulo"],
            contenido=request.POST["descripcion"],
            fecha_inicio_evento=request.POST["fecha"],
            imagen=request.FILES.get("imagen")
        )
        return redirect("eventos")

    return render(request, "vistas/crear_evento.html")


def eliminar_evento(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect("eventos")


def eliminar_blog(request, id):
    autor = blog.objects.get(id=id)
    autor.delete()
    return redirect("home")
