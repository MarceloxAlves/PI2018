from django.urls import path
from .views import *
urlpatterns = [
    path('', list_posts, name="posts"),
    path('add', add_post, name="add_post"),
]
