from django.urls import path


from .views import sign_in_user, register_user, logout_user, user_profile, egn_checker

urlpatterns = [
    path('signin/', sign_in_user, name='sign in'),
    path('signup/', register_user, name='sign up'),
    path('signout/', logout_user, name='sign out'),
    path('profile/', user_profile, name='profile'),
    path('egn_check/', egn_checker, name='egn checker'),

]
