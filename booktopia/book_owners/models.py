from datetime import date

from django.core.validators import MinLengthValidator, validate_email
from django.db import models

from booktopia.common.general_choices import GENDER_CHOICES

"""


"""


class Owner(models.Model):
    first_name = models.CharField(max_length=25, verbose_name='Име',
                                  validators=[MinLengthValidator(2)])
    middle_name = models.CharField(max_length=25,
                                   verbose_name='Презиме', blank=True)
    family_name = models.CharField(max_length=25, verbose_name='Фамилия',
                                   validators=[MinLengthValidator(2)])

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              verbose_name='Пол')
    date_of_birth = models.DateField(null=False, verbose_name='Дата на раждане')

    email = models.EmailField(verbose_name="Имейл адрес", max_length=100,
                              validators=[validate_email])
    mobile_phone = models.CharField(max_length=20, unique=True,
                                    verbose_name='Мобилен текефон')

    photo = models.ImageField(upload_to='photo_owners',
                              verbose_name='Снимка или аватар', null=True, blank=True)

    record_created_at = models.DateTimeField(auto_now_add=True, blank=True,
                                             null=True, verbose_name='Дата на създаване на записа')
    record_updated_at = models.DateTimeField(auto_now=True, blank=True,
                                             null=True, verbose_name='Дата на промяна на записа')

    def calculated_age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - \
               ((today.month, today.day) < (self.date_of_birth.month,
                                            self.date_of_birth.day))

    def __str__(self):
        return f'{self.first_name} {self.family_name} | {self.calculated_age()} г.'

    class Meta:
        verbose_name = 'Собственик'
        verbose_name_plural = 'Собственици'
        ordering = ['first_name']

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.middle_name = self.middle_name.title()
        self.family_name = self.family_name.title()
        self.email = self.email.lower()
        super().save(*args, **kwargs)

# TODO:

