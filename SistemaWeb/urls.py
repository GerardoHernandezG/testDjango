from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    #admin documentation
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #view url, con esto automaticamente carga todas las url que asignemos en urls.py de cada modulo
    url(r'', include('blog.urls')),

]
