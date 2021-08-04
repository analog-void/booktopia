"""
from django.db import models


class Reviews(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата-час')
    user_id = models.PositiveIntegerField()
    book_id = models.PositiveIntegerField(default=0)

    review = models.TextField(verbose_name='Съдържание на ревюто', null=True)
    rating = models.PositiveSmallIntegerField(verbose_name='Рейтинг')

    # record_created_at = models.DateTimeField(auto_now_add=True, blank=True,
    #                                          null=True, verbose_name='Дата на създаване на записа')
    # record_updated_at = models.DateTimeField(auto_now=True, blank=True,
    #                                          null=True, verbose_name='Дата на промяна на записа')

    def __str__(self):
        return str(self.timestamp.date())

    class Meta:
        verbose_name = 'Ревю'
        verbose_name_plural = 'Ревюта'
"""