from django import forms

from booktopia.books.models import Book
from booktopia.books.submodels.authors_model import Author
from booktopia.books.submodels.editions_model import Editions


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
        self._init_bootstrap()

        self.fields['name'].widget.attrs.update({'placeholder': 'Пълно име',
                                                 'title': 'Пълно име', })

        self.fields['price_for_rent'].widget.attrs.update({'placeholder': 'Минимална стойност: 1 лев',
                                                           'value': '1.00'})

        self.fields['synopsis'].widget.attrs.update(
            {'placeholder': 'Кратко читателско описание на съдържанието на книгата',
             'rows': 7, })

        self.fields['is_for_sale'].widget.attrs.update({'class': 'form-check-input', })
        self.fields['translated'].widget.attrs.update({'class': 'form-check-input', })
        self.fields['is_hidden'].widget.attrs.update({'class': 'form-check-input', })

        self.fields['cover_front'].widget.attrs.update({'class': '', })
        self.fields['cover_back'].widget.attrs.update({'class': '', })

        self.fields['tags'].widget.attrs.update({'class': '', })

    class Meta:
        model = Book
        # required_css_class = 'required'
        # error_css_class = 'error'

        fields = ('name',
                  # 'author_name',
                  'editions',
                  'synopsis',
                  'visual_condition',
                  'price_for_rent',
                  'release_year',
                  'cover_front',
                  'cover_back',

                  # ADDITIONAL FIELDS
                  'is_for_sale',
                  'price_for_sell',
                  'is_hidden',
                  'series',
                  'translated',
                  'original_name',
                  'edition_lang',
                  'release_number',

                  'edition_lang_orig',

                  'pages_count',
                  'measure_x',
                  'measure_y',
                  'weight_grams',

                  'isbn_code',
                  'oclc_code',
                  'tags',
                  )


class EditBookForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()  # cela on peut l'eviter

        self.fields['name'].widget.attrs.update({'placeholder': 'Пълно име',
                                                 'title': 'Пълно име', })

        self.fields['price_for_rent'].widget.attrs.update({'placeholder': 'Минимална стойност: 1 лев',
                                                           'value': '1.00'})

        self.fields['synopsis'].widget.attrs.update(
            {'placeholder': 'Кратко читателско описание на съдържанието на книгата',
             'rows': 7, })

        self.fields['is_for_sale'].widget.attrs.update({'class': 'form-check-input', })
        self.fields['translated'].widget.attrs.update({'class': 'form-check-input', })
        self.fields['is_hidden'].widget.attrs.update({'class': 'form-check-input', })

        self.fields['cover_front'].widget.attrs.update({'class': '', })
        self.fields['cover_back'].widget.attrs.update({'class': '', })

        self.fields['tags'].widget.attrs.update({'class': '', })

    class Meta:
        model = Book

        fields = ('name',
                  # 'author_name',
                  'editions',
                  'synopsis',
                  'visual_condition',
                  'price_for_rent',
                  'release_year',
                  'cover_front',
                  'cover_back',

                  # ADDITIONAL FIELDS
                  'is_for_sale',
                  'price_for_sell',
                  'is_hidden',
                  'series',
                  'translated',
                  'original_name',
                  'edition_lang',
                  'release_number',

                  'edition_lang_orig',

                  'pages_count',
                  'measure_x',
                  'measure_y',
                  'weight_grams',

                  'isbn_code',
                  'oclc_code',
                  'tags',
                  )


class BookCommentForm(forms.Form):
    pass


class AddAuthorForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = Author
        # exclude = ('name')
        fields = '__all__'


class EditAuthorForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = Author
        fields = '__all__'


class AddEditionForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = Editions
        fields = '__all__'


class EditEditionForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = Editions
        fields = '__all__'


"""
widgets = {
    'name': forms.TextInput(attrs={'class': 'form-control',
                                   'title': "test label",
                                   'placeholder': 'Enter todo text',
                                   'required': True,
                                   "template_name": None,
                                   },
                            ),

    'synopsis': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}),

    attrs={'class': 'form-control'}),  # queryset=Book.objects.all(),
}
"""

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
