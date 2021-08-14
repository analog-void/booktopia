from django.contrib.auth import get_user_model
from django.test import TestCase

from booktopia.accounts.models import BooktopiaUser, Profile
from booktopia.books.models import Book, Author, Editions

UserModel = get_user_model()


class ValidBook(TestCase):
    # valid_user = Profile.objects.get(pk=1)
    # valid_user = BooktopiaUser.objects.first()
    valid_editions = Editions.objects.first()
    valid_author = Author.objects.first()

    # valid_translated = '1'
    valid_name = 'The book name'
    valid_series = 'Galaktika'
    valid_original_name = 'The book original name'
    valid_current_status = 'СВОБОДНА'
    valid_release_year = 1999
    valid_visual_condition = 'ДОБРО'

    def test_when_all_is_correct_expect_success(self):
        book = Book(
            user=BooktopiaUser(id=1, email='xdex@free.fr', password='password'),
            # user=self.valid_user,
            name=self.valid_name,
            editions=self.valid_editions,
            series=self.valid_series,

            release_year=self.valid_release_year,
            author_name=self.valid_author,
        )


        book.full_clean()
        book.save()
        # with self.assertRaises(ValidationError) as context:
        #     book.full_clean()
        #     book.save()
        # self.assertIsNotNone(context.exception)
