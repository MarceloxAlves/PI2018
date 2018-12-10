from django.shortcuts import render, redirect, get_object_or_404
from .forms import *


def list_books(request):
    books = Book.objects.all()
    return render(request, "books.html", {'books': books})
# Create your views here.
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            return redirect('books')
    else:
        form = BookForm()
    return render(request, "add-book.html", {'form': form})

def edit_book(request, pk):
    post = get_object_or_404(Book,pk = pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=post)
        if form.is_valid():
            model_instance = form.save(commit=False)
            return redirect('books')
    else:
        form = BookForm(instance=post)
    return render(request, "edit-book.html", {'form': form , 'pk':pk})
