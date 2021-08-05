import egn
from django import forms
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

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


@login_required
def egn_checker(request):
    profile = Profile.objects.get(pk=request.user.id)
    egn_initial = profile.egn_number

    if request.method == 'POST':
        form_egn = EgnForm(
            request.POST,
            instance=profile,
        )

        if form_egn.is_valid():
            form_egn.save(commit=False)

            new_egn = form_egn.cleaned_data['egn_number']
            new_egn_check = egn.validate(new_egn)
            # egn_status = new_egn_check.split(' ')

            if new_egn_check:
                form_egn.save()
                return redirect('profile')

            else:
                raise ValidationError('Invalid EGN')

        """
            def egn_decompressor(self):
            egn_check = validate(self.egn_number)
            egn_status = egn_check.split(' ')
            if egn_status[2] == 'valid!':
                egn_details = parse(self.egn_number)
                egn_date_birth = f"{egn_details['year']}-{egn_details['month']}-{egn_details['day']}"
                egn_gender = str
        
        """
        # request.POST.
        # new_egn = request.get('egn_number')

        return redirect('profile')

    else:
        form_egn = EgnForm(instance=profile)

    context = {
        'form_egn': form_egn,
    }

    return render(request, 'accounts/egn_checker.html', context)

    # if not egn_initial or egn_initial <= 0: # TODO: a le fixer dans le modele
    #     pass
