from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from booktopia.accounts.forms import LoginForm


def sign_in_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user_cache
            login(request, user)
            return redirect('index')

    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/sign-in.html', context)


def register_user(request):
    pass


def logout_user(request):
    logout(request)
    return redirect('index')


