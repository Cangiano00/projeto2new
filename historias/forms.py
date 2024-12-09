from django.forms import ModelForm
from .models import Historia, Comment
from django import forms


class HistoriaForm(ModelForm):
    class Meta:
        model = Historia
        fields = ['name', 'capa','categoria', 'relato']
        labels = {
            'name':'Título da História Tenebrosa',
            'capa':'Quer adicionar uma ilustração de capa? (url)',
            'categoria':'Em quais categorias essa história se encaixa?        ',
            'relato':'Descreva todo o seu relato',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'autor',
            'texto',
        ]
        labels = {
            'autor': 'Usuário:',
            'texto': 'O que você tem a dizer?',
        }