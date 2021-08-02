from django.db import models


class Author(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата на създаване на записа')
    first_name = models.CharField(max_length=25, verbose_name='Име', )
    last_name = models.CharField(max_length=25, verbose_name='Фамилия', )
    pseudonym = models.CharField(max_length=25, verbose_name='Псевдоним', unique=True, null=True)

    date_of_birth = models.DateField(verbose_name='Рожденна Дата', blank=True, null=True)
    date_of_death = models.DateField(verbose_name='Починал на', blank=True, null=True)

    nationality = models.CharField(max_length=25, verbose_name='Националност', null=True)
    wiki_page = models.URLField(max_length=150, null=True, blank=True,
                                verbose_name="Страница в Уикипедиа или Биография")

    # TODO: Present age or dead at x years. Check if the authos if older than 100 years, then mark him/her as dead

    # record_created_at = models.DateTimeField(auto_now_add=True, blank=True,
    #                                          null=True, verbose_name='Дата на създаване на записа')
    # record_updated_at = models.DateTimeField(auto_now=True, blank=True,
    #                                          null=True, verbose_name='Дата на промяна на записа')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автори'
        ordering = 'first_name', 'last_name'