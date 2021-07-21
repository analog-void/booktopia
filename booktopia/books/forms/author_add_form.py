from django import forms


class AuthorAddForm(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    pseudonym = forms.CharField(max_length=25)
    date_of_birth = forms.DateField(required=False)
    date_of_death = forms.DateField(required=False)
    wiki_page = forms.URLField(required=False)

