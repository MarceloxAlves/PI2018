from django.urls import path
from .views import *
urlpatterns = [
    path('', list_books, name="books"),
    path('add', add_book, name="add_book"),
    path('<int:pk>/edit', edit_book, name="edit_book"),
]
