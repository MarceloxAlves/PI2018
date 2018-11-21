"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pools import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('question/<int:question_id>', views.exibir_question, name='exibir_question'),
    path('question/<int:question_id>/vote/<int:choice_id>', views.vote, name='votar'),
    path('question/<int:question_id>/result', views.result, name='result'),
    path('question/<int:question_id>/manage', views.manager, name='manage'),
    path('question/<int:question_id>/close', views.question_closed, name='question_closed'),
    path('question/<int:question_id>/attach/<int:choice_id>', views.choice_attach, name='choice_attach'),
    path('question/<int:question_id>/remove/<int:choice_id>', views.choice_remove, name='choice_remove'),
    path('question/add', views.question_add, name='question_add'),
    path('question/choice/add', views.choice_add, name='choice_add'),

]
