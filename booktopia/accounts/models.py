from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
# from datetime import date
from egn import parse

from .managers import BooktopiaUserManager
from ..common.general_choices import GENDER_CHOICES


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
        verbose_name='Последено влизане на потребителя'
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
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

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,
                              verbose_name='Пол', )

    date_of_birth = models.DateField(null=True, blank=True,
                                     verbose_name='Дата на раждане')

    egn_number = models.PositiveIntegerField(null=True, blank=True,
                                             verbose_name='Единен граждански номер')

    mobile_phone = models.CharField(max_length=20, unique=True,
                                    null=True, blank=True, default='+359 8',
                                    verbose_name='Мобилен телефон')

    photo = models.ImageField(upload_to='photo_owners',
                              null=True, blank=True,
                              verbose_name='Снимка или аватар', )

    record_created_at = models.DateTimeField(auto_now_add=True,
                                             blank=True, null=True,
                                             verbose_name='Дата на създаване на записа')

    record_updated_at = models.DateTimeField(auto_now=True,
                                             blank=True, null=True,
                                             verbose_name='Дата на промяна на записа')

    def get_egn_gender(self):
        egn_details = parse(self.egn_number)
        if egn_details['gender'] == 'Male':
            return 1
        else:
            return 2

    def get_egn_dob(self):
        egn_details = parse(self.egn_number)
        egn_dob = f"{egn_details['year']}-{egn_details['month']}-{egn_details['day']}"

        return egn_dob

    """
    {"year": 1978, "month": 10, "day": 15, "region_bg": 
    "\u0412\u0430\u0440\u043d\u0430", "region_en": "Varna", 
    "region_iso": "BG-03", "gender": "Male", "egn": "7810151027"}
    """


    def __str__(self):
        return f'{self.user} | {self.first_name} {self.family_name}'

    class Meta:
        verbose_name = 'Потребителски Акаунт'
        verbose_name_plural = 'Потребителски Акаунти'
        ordering = ['first_name']

    def save(self, *args, **kwargs):
        if not self.gender:
            self.gender = self.get_egn_gender()

        self.date_of_birth = self.get_egn_dob()
        super(Profile, self).save(*args, **kwargs)


from .signals import *
