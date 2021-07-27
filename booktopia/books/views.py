# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from booktopia.books.forms import AddBookForm, EditBookForm, BookCommentForm
from booktopia.books.models import Book


def index(request):
    return render(request, 'books/books_index.html')


def show_all_books(request):
    books = Book.objects.all()
    return render(request, 'books/books_all.html', {'books': books})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)

    # can_edit = book.user == request.user
    # can_delete = book.user == request.user
    is_owner = book.user == request.user

    context = {
        "book": book,
        'is_owner': is_owner,

    }
    return render(request, 'books/book_detail.html', context)


# @login_required
def add_book(request):
    # form = AddBookForm()
    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # TODO: a tester si c'est le bon truc - 1:38:00
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            # form.save()
            return redirect('all my books table')

    else:
        form = AddBookForm

    context = {
        'form': form
    }

    return render(request, 'books/book_add.html', context)


# @login_required
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = EditBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book index')
    else:
        form = EditBookForm(instance=book)

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'books/book_edit.html', context)


# @login_required
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('all my books table')
    else:
        context = {
            'book': book,
        }
    return render(request, 'books/book_delete.html', context)


"""
def like_book(request, pk):
    book_to_like = Book.objects.get(pk=pk)
    like = Like(
        book=book_to_like
    )
    like.save()
    return redirect('book detail', book_to_like.id)
"""


def book_comment(request, pk):
    form = BookCommentForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect('book detail', pk)
