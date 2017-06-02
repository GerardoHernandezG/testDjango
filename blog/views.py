from django.shortcuts import render
from blog.models import Articulos
from blog.models import Usuarios

from blog.forms import ArticuloForm
from blog.forms import ComentarioForm
from blog.forms import LoginForm
from blog.forms import UsuariosForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout
#from django.core.context_processors import csrf


def post_list(request):
    contenido = Articulos.objects.all()[:10]
    return render(request, 'blog/post_list.html', {'articulos': contenido})

def articulo(request, articulo_id=0):
    return render(request, 'blog/articulo.html', {'articulo': Articulos.objects.get(id=articulo_id)})

def crear(request):
    if request.POST:
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('blog')
    else:
        form = ArticuloForm()

    return render(request, 'blog/crear_articulo.html', {'form': form})


def agregar_comentario(request, articulo_id):
    articulo = Articulos.objects.get(id=articulo_id)

    if request.POST:
      form = ComentarioForm(request.POST)
      if form.is_valid():
        comentario = form.save(commit=False)

        comentario.fecha_pub = timezone.now()
        comentario.articulo = articulo

        comentario.save()

        return HttpResponseRedirect('blog/articulos/' % articulo_id)
    else:
        form = ComentarioForm()

    return render(request, 'blog/agregar_comentario.html', {'form': form})

def login(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username_post = form.cleaned_data['username']
            password_post = form.cleaned_data['password']
            try:
                query_bd = Usuarios.objects.get(username=username_post, password=password_post)
            except Usuarios.DoesNotExist:
                query_bd = None
            if query_bd is not None:
                if username_post == query_bd.username and password_post == query_bd.password:
                    return home(request, query_bd.username)
                else:
                    messages.error(request, 'Datos Incorrectos')
                    return HttpResponseRedirect('')
            else:
                messages.error(request, 'Datos Incorrectos')
                return HttpResponseRedirect('')
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})

def crear_usuario(request):
    if request.POST:
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario Agregado")
            return HttpResponseRedirect('')
        else:
            form = UsuariosForm()
    else:
        form = UsuariosForm()
    return render(request, 'login/agregar_usuario.html', {'form': form})

def home(request, username):
    return render(request, 'login/home.html', {'user': username})

def cerrar_sesion(request):
    logout(request)
    messages.success(request, "Sesión Finalizada")
    return HttpResponseRedirect('')
