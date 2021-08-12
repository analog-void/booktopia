from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from taggit.models import Tag

from booktopia.books.models import Book, Comments, CommentsAuthors, CommentsEditions
from booktopia.books.submodels.authors_model import Author
from booktopia.books.submodels.editions_model import Editions
from .forms import AddAuthorForm, EditAuthorForm, AddEditionForm, EditEditionForm, AuthorCommentForm, EditionCommentForm
from .forms import AddBookForm, EditBookForm, BookCommentForm
from ..accounts.models import Profile


def index(request):
    return render(request, 'books/books_index.html')


@login_required
def show_my_books(request):
    user = request.user.id
    books = Book.objects.filter(user_id=user)

    context = {
        'books': books,
    }
    return render(request, 'books/books_my.html', context)


class ShowAllBooks(ListView):
    template_name = 'books/books_all.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 5


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    comment = Comments.objects.filter(book_id=pk).order_by('-record_updated_at')
    tags = Tag.objects.filter(taggit_taggeditem_items__object_id=pk)
    profile = Profile.objects.all()
    is_owner = book.user == request.user

    if request.method == "POST":
        form = BookCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id_id = request.user.id
            comment.book_id_id = pk

            form.save()

            return redirect('book detail', pk)
    else:
        form = BookCommentForm

    context = {
        "book": book,
        'is_owner': is_owner,
        'comment': comment,
        'tags': tags,
        'profile': profile,
        'form': form,

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

    return render(request, 'books/book_edit.html', context)


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


##################################################################
##################################################################
##################################################################
# def show_all_authors(request):
#     author = Author.objects.all()
#
#     context = {
#         'author': author,
#     }
#     return render(request, "authors/authors_all.html", context)


class ShowAllAuthors(ListView):
    template_name = 'authors/authors_all.html'
    model = Author
    context_object_name = 'author'
    paginate_by = 4


def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    tags = Tag.objects.filter(taggit_taggeditem_items__object_id=pk)
    comments = CommentsAuthors.objects.filter(author_id_id=pk).order_by('-record_updated_at')
    books = Book.author_name

    if request.method == "POST":
        form = AuthorCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id_id = request.user.id
            comment.author_id_id = pk
            form.save()
        return redirect('author detail', pk)

    else:
        form = AuthorCommentForm

    context = {
        "author": author,
        'tags': tags,
        'books': books,
        'form': form,
        'comments': comments,
    }

    return render(request, 'authors/author_detail.html', context)


@login_required
def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save(commit=False)
            # book = Book.objects.get(pk=Book.pk)
            author.user = request.user

            author.save()

            return redirect('all my authors table')

    else:
        form = AddAuthorForm

    context = {
        'form': form
    }

    return render(request, 'authors/author_add.html', context)


@login_required
def edit_author(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == "POST":
        form = EditAuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()

            return redirect('all my authors table')

    else:
        form = EditAuthorForm(instance=author)

    context = {
        'form': form,
        'author': author,
    }

    return render(request, 'authors/author_edit.html', context)


@login_required
def delete_author(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == "POST":
        author.delete()
        return redirect('all my authors table')

    else:
        context = {
            'author': author,
        }
        return render(request, 'authors/author_delete.html', context)


##################################################################
##################################################################
##################################################################
# def show_all_editions(request):
#     editions = Editions.objects.all()
#
#     context = {
#         'editions': editions,
#     }
#     return render(request, 'editions/editions_all.html', context)

class ShowAllEditions(ListView):
    template_name = 'editions/editions_all.html'
    model = Editions
    context_object_name = 'editions'
    paginate_by = 4


def edition_detail(request, pk):
    edition = Editions.objects.get(pk=pk)
    comments = CommentsEditions.objects.filter(edition_id_id=pk).order_by('-record_updated_at')

    if request.method == "POST":
        form = EditionCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id_id = request.user.id
            comment.edition_id_id = pk
            form.save()
        return redirect('edition detail', pk)

    else:
        form = EditionCommentForm

    context = {
        "edition": edition,
        "comments": comments,
        "form": form,

    }

    return render(request, 'editions/editions_detail.html', context)


@login_required
def add_edition(request):
    if request.method == "POST":
        form = AddEditionForm(request.POST, request.FILES)
        if form.is_valid():
            edition = form.save(commit=False)
            # book = Book.objects.get(pk=Book.pk)
            edition.user = request.user

            edition.save()

            return redirect('all my editions table')

    else:
        form = AddEditionForm

    context = {
        'form': form
    }

    return render(request, 'editions/editions_add.html', context)


@login_required
def edit_edition(request, pk):
    edition = Editions.objects.get(pk=pk)
    if request.method == "POST":
        form = EditEditionForm(request.POST, request.FILES, instance=edition)
        if form.is_valid():
            form.save()

            return redirect('all my editions table')

    else:
        form = EditEditionForm(instance=edition)

    context = {
        'form': form,
        'edition': edition,
    }

    return render(request, 'editions/editions_edit.html', context)


@login_required
def delete_edition(request, pk):
    edition = Editions.objects.get(pk=pk)
    if request.method == "POST":
        edition.delete()
        return redirect('all my editions table')

    else:
        context = {
            'edition': edition,
        }
        return render(request, 'editions/editions_delete.html', context)


##################################################################
##################################################################

@login_required
def book_comment(request, pk):
    form = BookCommentForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect('book detail')


@login_required
def author_comment(request, pk):
    form = BookCommentForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect('author detail')


def ranking(request):
    return render(request, 'books/ranking.html')


"""
def like_book(request, pk):
    book_to_like = Book.objects.get(pk=pk)
    like = Like(
        book=book_to_like
    )
    like.save()
    return redirect('book detail', book_to_like.id)
"""
