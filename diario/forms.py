from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, EmailInput
from .models import Nota, Partilha, Cuidador, GrupoCare, DinamizadorConvidado


class NotaForm(ModelForm):
    class Meta:
        model = Nota
        fields = '__all__'
        widgets = {
            'nota': Textarea(attrs={'rows': 3, 'placeholder': 'Escreva uma nota...'}),
        }

class PartilhaForm(ModelForm):
    class Meta:
        model = Partilha
        fields = '__all__'
        widgets = {
            'partilha': Textarea(attrs={'rows': 3, 'placeholder': 'Escreva uma partilha...'}),
        }


class CuidadorForm(ModelForm):
    class Meta:
        model = Cuidador
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome ...'}),
            'sexo': Select(attrs={'class': 'form-control'}),
            'idade': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a idade ...'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o email ...'}),
            'nascimento': TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a data de nascimento ...'}),
            'nacionalidade': TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a nacionalidade ...'}),
            'escolaridade': Select(attrs={'class': 'form-control'}),
            'referenciacao': Select(attrs={'class': 'form-control'}),
            'regime': Select(attrs={'class': 'form-control'}),
            'localizacao': TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a localização ...'}),
            'grupoCare': Select(attrs={'class': 'form-control'}),
        }

class DinamizadorForm(ModelForm):
    class Meta:
        model = DinamizadorConvidado
        fields = {'nome','funcao'}
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome ...'}),
            'funcao': TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a função ...'}),

        }

class GrupoForm(ModelForm):
    class Meta:
        model = GrupoCare
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome do Grupo ...'}),
            'diagnostico': TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o diagnostico do Grupo ...'}),
            'localizacao': TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a Localização ...'}),
            'escolaridade': Select(attrs={'class': 'form-control'}),
            'referenciacao': Select(attrs={'class': 'form-control'}),
        }

