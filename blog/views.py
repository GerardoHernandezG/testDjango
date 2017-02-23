from django.shortcuts import render
from blog.models import Articulos

from blog.forms import ArticuloForm
from django.http import HttpResponseRedirect
#from django.core.context_processors import csrf


def post_list(request):
    contenido = Articulos.objects.all()[:10]
    return render(request, 'post_list.html', {'articulos': contenido})

def articulo(request, articulo_id=0):
    return render(request, 'articulo.html', {'articulo': Articulos.objects.get(id=articulo_id)})

def crear(request):
    if request.POST:
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('blog')
    else:
        form = ArticuloForm()

    return render(request, 'crear_articulo.html', {'form': form})
