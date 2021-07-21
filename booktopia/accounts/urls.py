from django.urls import path, include

from .views import sign_in_user, register_user, logout_user

urlpatterns = [
    path('signin/', sign_in_user, name='sign in'),
    path('signup/', register_user, name='sign up'),
    path('signout/', logout_user, name='sign out'),

]