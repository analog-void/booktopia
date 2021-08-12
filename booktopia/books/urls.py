from django.urls import path

from .views import index, book_detail, edit_book, add_book, delete_book, add_edition, ShowAllBooks, ranking, \
    show_my_books
from .views import author_detail, add_author, delete_author, edit_author, ShowAllAuthors
from .views import delete_edition, edition_detail, edit_edition, ShowAllEditions

urlpatterns = [
    # TODO: Iternal BOOK landing page
    path('', index, name='book index'),

    # BOOKS
    path('all-books/', ShowAllBooks.as_view(), name='all my books table'),
    path('my-books/', show_my_books, name='only my books'),

    path('book_detail/<int:pk>', book_detail, name='book detail'),
    path('add_book/', add_book, name='add new book'),
    path('edit_book/<int:pk>', edit_book, name='edit book'),
    path('delete_book/<int:pk>', delete_book, name='delete book'),

    # AUTHORS
    path('all-authors/', ShowAllAuthors.as_view(), name='all my authors table'),
    # path('all-authors/', show_all_authors, name='all my authors table'),

    path('authors_detail/<int:pk>', author_detail, name='author detail'),
    path('add_author/', add_author, name='add new author'),
    path('edit_author/<int:pk>', edit_author, name='edit author'),
    path('delete_author/<int:pk>', delete_author, name='delete author'),

    # EDITIONS
    path('all-editions/', ShowAllEditions.as_view(), name='all my editions table'),

    path('edition_detail/<int:pk>', edition_detail, name='edition detail'),
    path('add_edition/', add_edition, name='add new edition'),
    path('edit_edition/<int:pk>', edit_edition, name='edit edition'),
    path('delete_edition/<int:pk>', delete_edition, name='delete edition'),

    # All Rankings
    path('ranking/', ranking, name='ranking'),

    # Comments
    path('book_add_comment/<int:pk>', book_detail, name='new comment book'),
    path('author_add_comment/<int:pk>', author_detail, name='new comment author'),
    path('edition_add_comment/<int:pk>', edition_detail, name='new comment edition'),


]
