from django.urls import path

from .views import index, show_all_books, book_detail, edit_book, add_book, delete_book
from .views import show_all_authors, author_detail, add_author, delete_author, edit_author
from .views import show_all_editions

urlpatterns = [
    # TODO: Iternal BOOK landing page
    path('', index, name='book index'),

    # BOOKS
    path('all-books/', show_all_books, name='all my books table'),
    path('book_detail/<int:pk>', book_detail, name='book detail'),
    path('add_book/', add_book, name='add new book'),
    path('edit_book/<int:pk>', edit_book, name='edit book'),
    path('delete_book/<int:pk>', delete_book, name='delete book'),
    # path('all-books/', BookListView.as_view())

    # AUTHORS
    path('all-authors/', show_all_authors, name='all my authors table'),
    path('authors_detail/<int:pk>', author_detail, name='author detail'),
    path('add_author/', add_author, name='add new author'),
    path('edit_author/<int:pk>', edit_author, name='edit author'),
    path('delete_author/<int:pk>', delete_author, name='delete author'),

    # EDITIONS
    path('all-editions/', show_all_editions, name='all my editions table'),
    # path('edition_detail/<int:pk>', edition_detail, name='edition detail'),
    # path('add_edition/', add_edition, name='add new edition'),
    # path('edit_edition/<int:pk>', edit_edition, name='edit edition'),
    # path('delete_edition/<int:pk>', delete_edition, name='delete edition'),
]
