from django.shortcuts import render
from .models import Book


# Create your views here.

def books_index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books_index.html', context)


def book_detail(request, pk):
    book = Book.objects.all(pk=pk)
    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context)
