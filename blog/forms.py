from django import forms
from blog.models import Articulos
from blog.models import Comentario
from blog.models import Usuarios


class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulos
        fields = ['autor', 'titulo', 'texto', 'fecha']

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['nombre', 'cuerpo']

class LoginForm(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = ['username', 'password']

class UsuariosForm(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = ['username', 'password', 'email']
