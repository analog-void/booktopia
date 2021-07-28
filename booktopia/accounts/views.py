from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from booktopia.accounts.forms import LoginForm, RegisterForm


def sign_in_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book index')

    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/sign-in.html', context)


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save()
            login(request, user)
            
            # TODO: a creer un dashboard
            return redirect('all my books table')
        else:
            form = RegisterForm()
        context = {
            'form': form
        }

        return render(request, 'accounts/sign-up.html', context)


def logout_user(request):
    logout(request)
    return redirect('book index')
