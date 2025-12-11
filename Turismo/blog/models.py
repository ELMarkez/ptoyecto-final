from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



STATUS_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('REPROGRAMADO', 'Reprogramado'),
        ('CANCELADO', 'Cancelado'),
        ('FINALIZADO', 'Finalizado'),
    ]
    
class Evento(models.Model):
   
    titulo = models.CharField(max_length=250)
    imagen = models.ImageField(
        upload_to='eventos',
        verbose_name="Imagen",
        null=True,
        blank=True
    )
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    fecha_inicio_evento = models.DateTimeField(blank=True, null=True)
    fecha_fin_evento = models.DateTimeField(blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, default='PENDIENTE')
    
    def __str__(self):
        return self.titulo
    

class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField("nombre del usuario", max_length=200)
    apellido = models.CharField("apellido de la apersona", max_length=200)
    email = models.EmailField("correo electronico", unique=True)
    biografia = models.TextField("reseña personal", blank=True, null=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    autor_comentario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido_comentario = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(
        Evento,
        related_name="comentarios",
        on_delete=models.CASCADE
    )
    comentario_padre = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="respuestas",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.autor_comentario} - {self.contenido_comentario[:100]}"