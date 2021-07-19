from django.shortcuts import render

from booktopia.books.models import Book


def index(request):
    return render(request, 'books_index.html')


def show_all_books(request):
    books = Book.objects.all()
    return render(request, 'books_all.html', {'books': books})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book
    }
    return render(request, 'book_detail.html', context)


def add_book(request):
    pass


def edit_book(request, pk):
    pass
