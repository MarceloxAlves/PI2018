from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'sobrenome']
        widgets = {
            'nome': forms.TextInput(
                attrs= {
                    'class' : "form-control",
                    'placeholder' : "Digite o nome do usuário",
                }
            ),
            'sobrenome': forms.TextInput(
                attrs= {
                    'class' : "form-control",
                    'placeholder' : "Digite o nome do usuário",
                }
            )
        }