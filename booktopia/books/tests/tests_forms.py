from booktopia.books import forms


def test_with_standard_values_expect_success(self):
    data = {
        'name': 1,
        'price_for_rent': 10,
        'synopsis': 'the synopsis content',
        'is_for_sale': 1,
        'translated': 1,

    }

    form = forms.AddBookForm(data)

    self.assertTrue(form.is_valid())



