from django import forms
from .models import *
import re;

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        labels = {
            'title': 'Título',
            'text': 'Texto'
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': "form-control",
                }
            ),
            'text': forms.Textarea(
                attrs={
                    'class': "form-control",
                }
            )
        }


    """ def is_valid(self):
        black_list = {"Porra", "Puta"}
        valid = super(PostForm, self).is_valid()
        if not valid:
            return valid

        for palavra in black_list:
            if re.search('\\b'+ palavra +'\\b', self.cleaned_data['text'], re.IGNORECASE):
                return False

        return True """

    def clean_text(self):
        black_list = {"Porra", "Puta"}
        data = self.cleaned_data['text']
        for palavra in black_list:
            if re.search('\\b' + palavra + '\\b', data, re.IGNORECASE):
                raise forms.ValidationError("Seu texto contém palavras inadequeadas" )
        return data