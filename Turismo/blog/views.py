from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Evento, Autor, Comentario


def inicio(request):
    return render(request, 'home.html')


def eventos(request):
    lista = Evento.objects.order_by("fecha_creacion")
    return render(request, "eventos.html", {"eventos": lista})


def detalle_evento(request, id):
    evento = Evento.objects.get(id=id)
    return render(request, "detalle_evento.html", {"evento": evento})


def login_usuario(request):
    if request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("password")
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return redirect("inicio") 
    return render(request, "login.html")


def logout_usuario(request):
    logout(request)
    return redirect("inicio") 


def registro(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "registro.html", {"form": form})


@login_required
def crear_evento(request):
    if request.method == "POST":
        Evento.objects.create(
            autor_post=Autor.objects.get(user=request.user),
            titulo=request.POST["titulo"],
            contenido=request.POST["descripcion"],
            fecha_inicio_evento=request.POST["fecha"],
            imagen=request.FILES.get("imagen"),
            status=request.POST["status"]
        )
        return redirect("eventos")

    return render(request, "crear_evento.html")


def eliminar_evento(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect("eventos")


def eliminar_blog(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()
    return redirect("inicio")