from django.urls import path
from blog import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("eventos/", views.eventos, name="eventos"),
    path("detalle_evento/<int:id>/", views.detalle_evento, name="detalle_evento"),
    path("login/", views.login_usuario, name="login"),
    path("logout/", views.logout_usuario, name="logout"),
    path("registro/", views.registro, name="registro"),
    path("crear_evento/", views.crear_evento, name="crear_evento"),
    path("evento/eliminar/<int:id>/", views.eliminar_evento, name="eliminar_evento"),
    path("blog/eliminar/<int:id>/", views.eliminar_blog, name="eliminar_blog"),
]