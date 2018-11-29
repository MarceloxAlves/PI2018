from django import forms
from .models import *
import re;

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__",


    """ def is_valid(self):
        black_list = {"Porra", "Puta"}
        valid = super(PostForm, self).is_valid()
        if not valid:
            return valid

        for palavra in black_list:
            if re.search('\\b'+ palavra +'\\b', self.cleaned_data['text'], re.IGNORECASE):
                return False

        return True """

    def clean(self):
        black_list = {"Porra", "Puta"}
        for palavra in black_list:
            if re.search('\\b' + palavra + '\\b', self.cleaned_data['text'], re.IGNORECASE):
                raise forms.ValidationError("Seu texto contém palavras inadequeadas", code="text", )
        return self.cleaned_data