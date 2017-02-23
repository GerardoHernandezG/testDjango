from django import forms
from blog.models import Articulos


class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulos
        fields = ['autor', 'titulo', 'texto', 'fecha']
