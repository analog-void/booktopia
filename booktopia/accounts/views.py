import egn
# from django import forms
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from booktopia.accounts.forms import LoginForm, RegisterForm
from booktopia.accounts.models import Profile
from .forms import ProfileForm, EgnForm
from ..books.models import Book


def sign_in_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all my books table')

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
            # return redirect('all my books table')
            return redirect('egn checker')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/sign-up.html', context)


def logout_user(request):
    logout(request)
    return redirect('landing')


@login_required
def user_profile(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=profile)

    user_name = Book.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'user_name': user_name,
        'profile': profile,
    }

    return render(request, 'accounts/profile.html', context)


# @login_required
def egn_checker(request):
    profile = Profile.objects.get(pk=request.user.id)
    # egn_initial = profile.egn_number

    is_profile_completed = None
    if profile.egn_number and profile.first_name and profile.family_name and profile.mobile_phone:
        is_profile_completed = True

    if request.method == 'POST':
        form_egn = EgnForm(
            request.POST,
            instance=profile,
        )

        if form_egn.is_valid():
            form_egn.save(commit=False)

            new_egn = form_egn.cleaned_data['egn_number']

            # IF EGN IS SUBMITTED NULL
            if not new_egn:
                return redirect('egn checker')

            new_egn_check = egn.validate(new_egn)

            if new_egn_check:
                form_egn.save()
                return redirect('profile')

            else:
                return redirect('egn checker')
                # raise ValidationError('Invalid EGN')

        else:
            return redirect('egn checker')

    else:
        form_egn = EgnForm(instance=profile)

    context = {
        'form_egn': form_egn,
        'is_profile_completed': is_profile_completed,
    }

    # return render(request, 'accounts/profile.html', context)
    return render(request, 'accounts/egn_checker.html', context)


# @login_required
class ShowAllProfiles(ListView):
    template_name = 'accounts/profile_all.html'
    model = Profile
    context_object_name = 'profile'
    paginate_by = 10


"""
DUMMY USERS
xxx@beta.com
xxx@beta2.com
alpha@gamma.com

PassWord1
"""
