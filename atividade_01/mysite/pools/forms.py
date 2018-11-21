from django import forms
from .models import *


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        widgets = {
            'question_text': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Type your question",
                }
            ),
            'pub_date': forms.DateInput(
                attrs={
                    'class': "form-control",
                    'type': 'date',
                }
            )
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'question']
        widgets = {
            'choice_text': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Type your choice",
                }
            ),
            'question': forms.Select(
                attrs={
                    'class': "form-control",
                }
            )
        }
