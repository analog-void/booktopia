from datetime import date

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
from egn import parse

from .managers import BooktopiaUserManager
from .validators import *
from ..common.general_choices import GENDER_CHOICES


class BooktopiaUser(AbstractBaseUser, PermissionsMixin):
    # FIXME: d'ou cela vient et pqoi ca fait tout planter ...
    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)

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
                                  # validators=[MinLengthValidator(3),
                                  #             MaxLengthValidator(25),
                                  #             validate_not_null,
                                  #             ]
                                  )

    middle_name = models.CharField(max_length=25,
                                   null=True, blank=True,
                                   verbose_name='Презиме', )

    family_name = models.CharField(max_length=25, verbose_name='Фамилия',
                                   null=True, blank=True,
                                   # validators=[MinLengthValidator(2)],
                                   )

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,
                              verbose_name='Пол', )

    date_of_birth = models.DateField(null=True, blank=True,
                                     verbose_name='Дата на раждане')

    egn_number = models.PositiveIntegerField(null=True, blank=True,
                                             verbose_name='Единен граждански номер')

    region_of_birth = models.CharField(max_length=20, null=True, blank=True,
                                       verbose_name='Роден в област')

    astrological_sign = models.CharField(max_length=20, null=True, blank=True,
                                         verbose_name='Зодиакален знак')

    # FIXME: VERIF - UNIQUE NUMBER - , unique=True,
    mobile_phone = models.CharField(max_length=20,
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

    @property
    def user_data_progress(self):
        # total sum = 100%
        egn = 16.66 if self.egn_number else 0
        first_name = 16.66 if self.first_name else 0
        middle_name = 16.66 if self.middle_name else 0
        family_name = 16.66 if self.family_name else 0
        mobile_phone = 16.66 if self.mobile_phone else 0

        # FIXME: DEFAULT PROFILE PHOTO
        profile_photo = 16.7 if not self.photo.name == 'profile-default.jpg' else 0

        somme = egn + first_name + middle_name + family_name + mobile_phone + profile_photo
        return somme

    @property
    def user_ranking(self):
        ranking = 'Гражданин на Буктопия'

        comments = self.user.comments_set.count()
        books = self.user.book_set.count()

        if comments and books:
            ranking = 'Продавач на енциклопедии'
        if comments > 10 and books > 3:
            ranking = 'Стажант'
        elif comments > 20 and books > 10:
            ranking = 'Чиновник'
        elif comments > 30 and books > 15:
            ranking = 'Писател'
        elif comments > 40 and books > 15:
            ranking = 'Писател'
        elif comments > 50 and books > 20:
            ranking = 'Главен Счетоводител'
        elif comments > 60 and books > 25:
            ranking = 'Книговезец'
        elif comments > 70 and books > 30:
            ranking = 'Коректор Печат'
        elif comments > 80 and books > 35:
            ranking = 'Помощник библиотекар'
        elif comments > 90 and books > 40:
            ranking = 'Библиотекар'
        elif comments > 100 and books > 45:
            ranking = 'Старши библиотекар'
        elif comments > 110 and books > 50:
            ranking = 'Архивист'
        elif comments > 120 and books > 55:
            ranking = 'Велик архивист'
        elif comments > 130 and books > 60:
            ranking = 'Редактор'
        elif comments > 140 and books > 65:
            ranking = 'Главен редактор'
        elif comments > 150 and books > 70:
            ranking = 'Издател'
        elif comments > 160 and books > 75:
            ranking = 'Почетен издател'
        elif comments > 170 and books > 80:
            ranking = 'Графолог'
        elif comments > 180 and books > 85:
            ranking = 'Лексикоман Любител'
        elif comments > 190 and books > 90:
            ranking = 'Напреднал Лексикоман'
        elif comments > 200 and books > 95:
            ranking = 'Велик Лексикоман'
        elif comments > 215 and books > 100:
            ranking = 'Шампион по Судоку'
        elif comments > 225 and books > 150:
            ranking = 'Чудовището от речника'
        elif comments > 235 and books > 200:
            ranking = 'Преводач на Хари Потър'
        elif comments > 245 and books > 250:
            ranking = 'Преводач на Франц Кафка'
        elif comments > 255 and books > 300:
            ranking = 'Преводач на Джеймс Джойс'
        elif comments > 265 and books > 350:
            ranking = 'Книжен плъх'
        elif comments > 275 and books > 400:
            ranking = 'Почетен Гражданин на Буктопия'
        elif comments > 285 and books > 450:
            ranking = 'Буктопия Гуру'
        elif comments > 300 and books > 500:
            ranking = 'Велик Везир на Буктопия'

        return ranking

    def clean(self):
        if not self.first_name or \
                len(self.first_name) < 3 or \
                len(self.first_name) >= 25:
            raise ValidationError(
                {'first_name': "Името трябва да е най-малко 3 и най-много 25 символа"})

        if not self.family_name or \
                len(self.family_name) < 3 or \
                len(self.family_name) >= 25:
            raise ValidationError(
                {'family_name': "Фамилията трябва да е най-малко 3 и най-много 25 символа"})

        if not self.mobile_phone or \
                len(self.mobile_phone) < 4 or \
                len(self.mobile_phone) >= 17:
            # TODO: REGEX validator
            raise ValidationError(
                {'mobile_phone': "Номерът на телефона трябва да е най-малко 4 и не повече от 17 символа"})

    def get_egn_gender(self):
        egn_details = parse(self.egn_number)
        if egn_details['gender'] == 'Male':
            return 'M'
        else:
            return 'F'

    def get_egn_dob(self):
        egn_details = parse(self.egn_number)
        egn_dob = f"{egn_details['year']}-{egn_details['month']}-{egn_details['day']}"
        return egn_dob

    def get_birth_region(self):
        egn_details = parse(self.egn_number)
        region = egn_details['region_bg']
        return region

    def get_astro_sign(self):
        egn_details = parse(self.egn_number)
        day = egn_details['day']
        month = egn_details['month']
        astro_sign = ''

        if month == 12:
            astro_sign = 'Стрелец' if (day < 22) else 'Козирог'

        elif month == 1:
            astro_sign = 'Козирог' if (day < 20) else 'Водолей'

        elif month == 2:
            astro_sign = 'Водолей' if (day < 19) else 'Риби'

        elif month == 3:
            astro_sign = 'Риби' if (day < 21) else 'Овен'

        elif month == 4:
            astro_sign = 'Овен' if (day < 20) else 'Телец'

        elif month == 5:
            astro_sign = 'Телец' if (day < 21) else 'Близнаци'

        elif month == 6:
            astro_sign = 'Близнаци' if (day < 21) else 'Рак'

        elif month == 7:
            astro_sign = 'Рак' if (day < 23) else 'Лъв'

        elif month == 8:
            astro_sign = 'Лъв' if (day < 23) else 'Дева'

        elif month == 9:
            astro_sign = 'Дева' if (day < 23) else 'Везни'

        elif month == 10:
            astro_sign = 'Везни' if (day < 23) else 'Скорпион'

        elif month == 11:
            astro_sign = 'Скорпион' if (day < 22) else 'Стрелец'

        return astro_sign

    # {"year": 1978, "month": 10, "day": 15, "region_bg":
    # "\u0412\u0430\u0440\u043d\u0430", "region_en": "Varna",
    # "region_iso": "BG-03", "gender": "Male", "egn": "7810151027"}

    def profile_calculated_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - \
              ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return f'{age} години'

    def __str__(self):
        return f'{self.user} | {self.first_name} {self.family_name}'

    class Meta:
        verbose_name = 'Потребителски Акаунт'
        verbose_name_plural = 'Потребителски Акаунти'
        ordering = ['first_name']

    def save(self, *args, **kwargs):
        if self.egn_number:
            self.gender = self.get_egn_gender()
            self.region_of_birth = self.get_birth_region()
            self.astrological_sign = self.get_astro_sign()
            self.date_of_birth = self.get_egn_dob()

        super(Profile, self).save(*args, **kwargs)


from .signals import *
