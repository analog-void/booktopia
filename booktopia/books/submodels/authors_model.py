from datetime import date

from django.db import models

from booktopia.common.countries import COUNTRIES_BG


class Author(models.Model):
    first_name = models.CharField(max_length=25, verbose_name='Име', )
    last_name = models.CharField(max_length=25, verbose_name='Фамилия', )
    pseudonym = models.CharField(max_length=25, verbose_name='Псевдоним',
                                 unique=True, null=True, blank=True)

    date_of_birth = models.DateField(verbose_name='Рожденна Дата', blank=True, null=True)
    date_of_death = models.DateField(verbose_name='Починал на', blank=True, null=True)

    nationality = models.CharField(max_length=25, verbose_name='Националност',
                                   null=True, blank=True, choices=COUNTRIES_BG)

    wiki_page = models.URLField(max_length=150, null=True, blank=True,
                                verbose_name="Страница в Уикипедиа или Биография")

    def author_calculated_age(self):
        today = date.today()
        if self.date_of_birth and not self.date_of_death:
            age = today.year - self.date_of_birth.year - \
                  ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

            if age >= 100:
                age = "n/a"
                return age
            else:
                return f'{str(age)} г.'
        elif self.date_of_birth and self.date_of_death:
            age = self.date_of_death.year - self.date_of_birth.year - \
                  ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
            return f'{age} г. [✝]'
        else:
            return "n/a"

    record_created_at = models.DateTimeField(auto_now_add=True, blank=True,
                                             null=True, verbose_name='Дата на създаване на записа')
    record_updated_at = models.DateTimeField(auto_now=True, blank=True,
                                             null=True, verbose_name='Дата на промяна на записа')

    def author_book_count(self):
        num_books = self.book_set.count()
        return num_books

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.author_calculated_age()}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автори'
        ordering = 'first_name', 'last_name'
