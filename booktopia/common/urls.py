from django.urls import path

from booktopia.common.views import landing_page

urlpatterns = [
    path('', landing_page, name='landing'),
]
