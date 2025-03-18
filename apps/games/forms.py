from django import forms
from .models import Jogo, ImagemJogo

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        exclude = ['JogoID','ExibirHome',]
        labels = {
            'Nome': 'Nome do Jogo',
            'CategoriaID': 'Categoria',
            'Ordem': 'Ordem de exibição',
        }

        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'form-control'}),
            'Ordem': forms.TextInput(attrs={'class': 'form-control'}),
            'CategoriaID': forms.TextInput(attrs={'class': 'form-control'}),
        }