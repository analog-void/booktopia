from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from booktopia.accounts.models import Profile

UserModel = get_user_model()


class BootstrapFormMixin:
    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
            }


class LoginForm(forms.Form, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    user = None
    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Грешно потребителско име или парола')

    def save(self):
        return self.user


class RegisterForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = UserModel
        fields = ('email',)


class ProfileForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    def fields_checkups(self):
        first_name = self.cleaned_data['first_name']
        if not first_name:
            raise ValidationError('Празно потребителско име')

    class Meta:
        model = Profile

        fields = ('first_name',
                  'middle_name',
                  'family_name',
                  # 'gender',
                  # 'date_of_birth',
                  # 'egn_number',
                  'mobile_phone',
                  'photo',
                  )


class EgnForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = Profile
        fields = ('egn_number',)


"""

class RenewBookModelForm(ModelForm):
    def clean_due_back(self):
       data = self.cleaned_data['due_back']

       # Check if a date is not in the past.
       if data < datetime.date.today():
           raise ValidationError(_('Invalid date - renewal in past'))

       # Check if a date is in the allowed range (+4 weeks from today).
       if data > datetime.date.today() + datetime.timedelta(weeks=4):
           raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

       # Remember to always return the cleaned data.
       return data

    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back': _('Renewal date')}
        help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3).')}

"""
