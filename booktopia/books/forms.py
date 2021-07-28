from django import forms

from booktopia.books.models import Book

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

"""
       _content_type = forms.ModelChoiceField(
            queryset=ContentType.objects.filter(id__in=content_types),
            empty_label=None,
            label=capfirst(_("model")),

"""


class BootstrapFormMixin:
    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                # 'for': "typeNumber",
            }


class AddBookForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()  # cela on peut l'eviter

        self.fields['name'].widget.attrs.update({'placeholder': 'Пълно име',
                                                 'title': 'New title',
                                                 'aria-describedby': "textExample1"})
        self.fields['price_for_rent'].widget.attrs.update({'placeholder': 'Минимална стойност: 1 лев',
                                                           'value': ''})
        self.fields['synopsis'].widget.attrs.update({'placeholder': 'Кратко и привлекателно описание на книгата',
                                                     'rows': 7,})

# TODO: a ajouter plusieurs auteurs par livre,
# agrandir le synopsis
# Стойност на гаранцията (лв.): - Add value
# Release year - DATE type
#
    class Meta:
        model = Book
        # required_css_class = 'required'
        # error_css_class = 'error'

        fields = ('name',
                  'author_name',
                  'editions',
                  'synopsis',
                  'visual_condition',
                  'price_for_rent',
                  'release_year',
                  'cover_front',
                  'cover_back',
                  )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'title': "test label",
                                           'placeholder': 'Enter todo text',
                                           'required': True,
                                           "template_name": None,
                                           },
                                    ),

            'synopsis': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}),

            # attrs={'class': 'form-control'}),  # queryset=Book.objects.all(),
        }


# class AddBookForm(forms.Form):
#     name = forms.CharField()
#     editions = forms.CharField()
#     series = forms.CharField()
#
#     release_year = forms.CharField()
#     pages_count = forms.CharField()
#     weight_grams = forms.IntegerField()
#
#     # a revoir a cote
#     cover_front = forms.CharField()
#     cover_back = forms.CharField()


class EditBookForm(forms.Form):
    pass


class BookCommentForm(forms.Form):
    pass
