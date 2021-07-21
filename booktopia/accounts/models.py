from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from .managers import BooktopiaUserManager
from ..common.general_choices import GENDER_CHOICES


# from datetime import date

class BooktopiaUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        max_length=100,
        verbose_name='Имейл Адрес'
    )

    # BOOLS
    is_staff = models.BooleanField(
        default=False,
    )

    is_superuser = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_owner = models.BooleanField(
        default=True,
    )

    is_seller = models.BooleanField(
        default=False,
    )

    is_runner = models.BooleanField(
        default=False,
    )

    last_login = models.DateTimeField(
        auto_now=True,
        # default=timezone.now,
        verbose_name='Последено влизане на потребителя'
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        # auto_created=True,
        # default=timezone.now,
        # auto_now=True,
        # blank=True,
        verbose_name='Дата на създаване на акаунта'
    )

    USERNAME_FIELD = 'email'

    objects = BooktopiaUserManager()


class Profile(models.Model):
    user = models.OneToOneField(
        BooktopiaUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

    first_name = models.CharField(max_length=25, verbose_name='Име',
                                  null=True, blank=True,
                                  validators=[MinLengthValidator(2)])

    middle_name = models.CharField(max_length=25,
                                   null=True, blank=True,
                                   verbose_name='Презиме', )

    family_name = models.CharField(max_length=25, verbose_name='Фамилия',
                                   null=True, blank=True,
                                   validators=[MinLengthValidator(2)], )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              verbose_name='Пол', )

    date_of_birth = models.DateField(null=True, blank=True,
                                     verbose_name='Дата на раждане')

    mobile_phone = models.CharField(max_length=20, unique=True,
                                    null=True, blank=True,
                                    verbose_name='Мобилен текефон')

    photo = models.ImageField(upload_to='photo_owners',
                              null=True, blank=True,
                              verbose_name='Снимка или аватар', )

    record_created_at = models.DateTimeField(auto_now_add=True,
                                             blank=True, null=True,
                                             verbose_name='Дата на създаване на записа')

    record_updated_at = models.DateTimeField(auto_now=True,
                                             blank=True, null=True,
                                             verbose_name='Дата на промяна на записа')

    # def calculated_age(self):
    #     today = date.today()
    #     return today.year - self.date_of_birth.year - \
    #            ((today.month, today.day) < (self.date_of_birth.month,
    #                                         self.date_of_birth.day))

    def __str__(self):
        return f'{self.first_name} {self.family_name}'
        # f' | {self.calculated_age()} г.'

    class Meta:
        verbose_name = 'Потребителски Акаунт'
        verbose_name_plural = 'Потребителски Акаунти'
        ordering = ['first_name']
    #
    # def save(self, *args, **kwargs):
    #     self.first_name = self.first_name.title()
    #     self.middle_name = self.middle_name.title()
    #     self.family_name = self.family_name.title()
    #     super().save(*args, **kwargs)


from .signals import *
