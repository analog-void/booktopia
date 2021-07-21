from django.conf.urls.static import static # je sais pas si c'est le bon import
from django.contrib import admin
from django.urls import path, include

from booktopia import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('grappelli-docs/', include('grappelli.urls_docs')), # grappelli docs URLS

    # path('', ,)
    # Booktopia main URLs
    # TODO: Landing Page

    path('book/', include('booktopia.books.urls')),
    path('owner/', include('booktopia.book_owners.urls')),
    path('shopper/', include('booktopia.book_shoppers.urls')),
    path('hub/', include('booktopia.book_hubs.urls')),
    path('runner/', include('booktopia.book_runners.urls')),
    path('account/', include('booktopia.accounts.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
