from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^blog/', views.post_list, name='blog'),
    url(r'^articulos/(?P<articulo_id>\d+)/$', views.articulo),
    url(r'^crear/', views.crear, name='crear'),
    url(r'^/agregar_comentario/(?P<articulo_id>\d+)/$', views.agregar_comentario),

    #login
    url(r'^login/', views.login),
    url(r'^crear_usuario/', views.crear_usuario),
    url(r'^home/', views.home),
    url(r'^cerrar_sesion/', views.cerrar_sesion),
]
