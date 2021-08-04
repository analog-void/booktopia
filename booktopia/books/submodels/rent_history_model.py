from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models

from booktopia.books.models import Book

UserModel = get_user_model()

RENT_DURATION_DAYS = (
    (7, 7),
    (14, 14),
    (21, 21),
    (28, 28),
)

RENT_STATUS = (
    ('PENDING', 'ПЛАНИРАНА'),
    ('EFFECTIVE', 'ТЕКУЩА'),
    ('TERMINATED', 'ПРИКЛЮЧИЛА'),
    ('UNATTRACTIVE', 'БЕЗ ПРОДЪЛЖЕНИЕ'),
)


class RentHistory(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE,
                                null=True, blank=True,
                                verbose_name='ID Потребител')

    book_id = models.ForeignKey(Book, on_delete=models.CASCADE,
                                null=True, blank=True,
                                verbose_name='ID книга')

    date_from = models.DateField(blank=True, null=True,
                                 verbose_name='От дата:')

    rented_for_days = models.IntegerField(default=14,
                                          verbose_name='Заета за дни:',
                                          choices=RENT_DURATION_DAYS, )

    rent_status = models.CharField(max_length=12,
                                   choices=RENT_STATUS, default='NULL',
                                   null=True, blank=True)

    def rent_end_date(self):
        return self.date_from + timedelta(self.rented_for_days)

    # ???
    date_to = models.DateField(blank=True, null=True,
                               verbose_name='До дата (авто)')

    # rent_duration = models
    rent_event_comment = models.TextField(null=True, blank=True,
                                          verbose_name='Коментар по заемането')

    degradations = models.TextField(null=True, blank=True,
                                    verbose_name='Деградации в качеството на книгата')

    record_created_at = models.DateTimeField(auto_now_add=True, blank=True,
                                             null=True, verbose_name='Дата на създаване на записа')

    record_updated_at = models.DateTimeField(auto_now=True, blank=True,
                                             null=True, verbose_name='Дата на промяна на записа')

    def __str__(self):
        return f'{self.book_id} {self.user_id} [от {self.date_from} до {self.rent_end_date()}]'

    class Meta:
        verbose_name = 'История на заеманията'
        verbose_name_plural = 'История на заеманията'
        ordering = 'date_from',

    def save(self, *args, **kwargs):
        self.date_to = self.rent_end_date()
        super(RentHistory, self).save(*args, **kwargs)
