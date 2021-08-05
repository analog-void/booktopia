from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from booktopia import settings
from booktopia.common.views import landing_page

urlpatterns = [
    path('', landing_page, name='landing'),
    path('admin/', admin.site.urls, name='admin'),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('grappelli-docs/', include('grappelli.urls_docs')),  # grappelli docs URLS

    path('book/', include('booktopia.books.urls')),

    # TODO: A LE MERGER AVEC PROFILE
    path('owner/', include('booktopia.book_owners.urls')),

    path('shopper/', include('booktopia.book_shoppers.urls')),
    path('hub/', include('booktopia.book_hubs.urls')),
    path('runner/', include('booktopia.book_runners.urls')),
    path('account/', include('booktopia.accounts.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
