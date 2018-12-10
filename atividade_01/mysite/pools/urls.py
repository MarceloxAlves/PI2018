from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="questions"),
    path('question/<int:question_id>', exibir_question, name='exibir_question'),
    path('question/<int:question_id>/vote/<int:choice_id>', vote, name='votar'),
    path('question/<int:question_id>/result', result, name='result'),
    path('question/<int:question_id>/manage', manager, name='manage'),
    path('question/<int:question_id>/close', question_closed, name='question_closed'),
    path('question/<int:question_id>/attach/<int:choice_id>', choice_attach, name='choice_attach'),
    path('question/<int:question_id>/remove/<int:choice_id>', choice_remove, name='choice_remove'),
    path('question/add', question_add, name='question_add'),
    path('question/choice/add', choice_add, name='choice_add'),
]