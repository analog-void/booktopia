from django.urls import path

from .views import index, show_all_books, book_detail, edit_book, add_book, delete_book

urlpatterns = [
    # TODO: Iternal BOOK landing page
    path('', index, name='book index'),

    path('all-books/', show_all_books, name='all my books table'),
    path('book_detail/<int:pk>', book_detail, name='book detail'),
    path('add_book/', add_book, name='add new book'),
    path('edit_book/<int:pk>', edit_book, name='edit book'),
    path('delete_book/<int:pk>', delete_book, name='delete book'),
    # path('all-books/', BookListView.as_view())

]
