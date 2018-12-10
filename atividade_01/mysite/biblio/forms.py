from django import forms
from .models import *
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            )
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
