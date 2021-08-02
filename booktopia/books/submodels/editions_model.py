from django.db import models

from booktopia.common.countries import COUNTRIES_BG


class Editions(models.Model):
    name = models.CharField(max_length=50, verbose_name='Име', unique=True)
    address = models.TextField(verbose_name='Пощенски адрес', blank=True)
    country = models.CharField(max_length=100, verbose_name='Държава', choices=COUNTRIES_BG)

    # FIXME - a revoir bien les pats de uploads
    # TODO: Tester er immplementer l'image upload /// resize
    logo = models.ImageField(upload_to='', blank=True)
    stars = models.PositiveSmallIntegerField(default=0, null=True)
    web_address = models.URLField(max_length=150, null=True, blank=True, verbose_name="Уеб Сайт")

    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата на създаване на записа')

    # record_created_at = models.DateTimeField(auto_now_add=True, blank=True,
    #                                          null=True, verbose_name='Дата на създаване на записа')
    # record_updated_at = models.DateTimeField(auto_now=True, blank=True,
    #                                          null=True, verbose_name='Дата на промяна на записа')

    def __str__(self):
        return self.name.upper()

    class Meta:
        verbose_name = 'Издателство'
        verbose_name_plural = 'Издателства'
        ordering = ("name",)





