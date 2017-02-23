from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^blog/', views.post_list, name='blog'),
    url(r'^articulos/(?P<articulo_id>\d+)/$', views.articulo),
    url(r'^crear/', views.crear, name='crear'),
]
