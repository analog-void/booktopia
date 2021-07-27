from django import forms

"""
(
required = True,
label = 'label string',
initial = 199.99,
widget = forms.Textarea(attrs={})


name = forms.CharField(max_length=100)
authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())


        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter todo text',
            }


) 
"""


class AddBookForm(forms.Form):
    name = forms.CharField()
    editions = forms.CharField()
    series = forms.CharField()

    release_year = forms.CharField()
    pages_count = forms.CharField()
    weight_grams = forms.IntegerField()

    # a revoir a cote
    cover_front = forms.CharField()
    cover_back = forms.CharField()


class EditBookForm(forms.Form):
    pass


class BookCommentForm(forms.Form):
    pass
