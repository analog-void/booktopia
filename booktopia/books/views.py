from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from taggit.models import Tag

from booktopia.books.forms import AddBookForm, EditBookForm, BookCommentForm
from booktopia.books.models import Book, Comments


def index(request):
    return render(request, 'books/books_index.html')


def show_all_books(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'books/books_all.html', context)


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    comment = Comments.objects.filter(book_id=pk)
    tags = Tag.objects.filter(taggit_taggeditem_items__object_id=pk)

    is_owner = book.user == request.user

    context = {
        "book": book,
        'is_owner': is_owner,
        'comment': comment,
        'tags': tags,
    }
    return render(request, 'books/book_detail.html', context)


@login_required
def add_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            # book = Book.objects.get(pk=Book.pk)
            book.user = request.user

            book.cover_front = form.cleaned_data['cover_front']
            book.cover_back = form.cleaned_data['cover_back']

            book.save()
            form.save_m2m()

            return redirect('all my books table')

    else:
        form = AddBookForm

    context = {
        'form': form
    }

    return render(request, 'books/book_add.html', context)


@login_required
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = EditBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()

            return redirect('all my books table')

    else:
        form = EditBookForm(instance=book)

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'books/book_delete.html', context)


@login_required
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


@login_required
def book_comment(request, pk):
    form = BookCommentForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect('book detail', pk)


"""
def like_book(request, pk):
    book_to_like = Book.objects.get(pk=pk)
    like = Like(
        book=book_to_like
    )
    like.save()
    return redirect('book detail', book_to_like.id)
"""
