from django.contrib import admin
from .models import Autor, Categoria, Evento, Comentario


admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Evento)
admin.site.register(Comentario)