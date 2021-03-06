import os
import random
import string
from datetime import datetime

import qrcode
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
# from django.db import models
from django.utils.html import mark_safe  # for Image Tags and book previews
#
from taggit.managers import TaggableManager

from booktopia.book_owners.models import Owner
from booktopia.common.countries import LANGUAGES_BG
from booktopia.common.general_choices import BOOK_RELEASE, BOOK_CONDITION, BOOK_CURRENT_STATUS
from booktopia.settings import MEDIA_ROOT
# IMPORTING SPLITED INITIAL MODEL FILE
#
from .submodels.authors_model import *
from .submodels.editions_model import *
from .submodels.status_model import *

#


UserModel = get_user_model()


class Book(models.Model):
    # Section Nom
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        default=1,
        verbose_name='Потребител'
    )

    name = models.CharField(max_length=200, verbose_name='Име на книгата')

    editions = models.ForeignKey(Editions, on_delete=models.DO_NOTHING,
                                 verbose_name='Издателска къща', default='')

    series = models.CharField(max_length=100, verbose_name='Поредица',
                              null=True, blank=True)

    translated = models.BooleanField(default=False, verbose_name='Преведена')

    original_name = models.CharField(max_length=200, verbose_name='Оригинално име', blank=True)

    edition_lang = models.CharField(max_length=3, choices=LANGUAGES_BG,
                                    verbose_name='Език на изданието',
                                    default='Български език',
                                    blank=True)

    edition_lang_orig = models.CharField(max_length=3, choices=LANGUAGES_BG,
                                         verbose_name='Оригинален Език',
                                         blank=True)

    book_current_status = models.CharField(max_length=25, default='F',
                                           verbose_name='Актуално състояние на книгата',
                                           choices=BOOK_CURRENT_STATUS)

    catalog_num = models.CharField(max_length=100, verbose_name='Вътрешен каталожен номер',
                                   null=True, blank=True,
                                   help_text="Каталожен номер по десетична система. Полето е задължително",
                                   default=None)

    isbn_code = models.CharField(max_length=15, verbose_name='ISBN', blank=True, null=True)

    oclc_code = models.CharField(max_length=15, verbose_name='OCLC', blank=True, null=True)

    synopsis = models.TextField(blank=True, null=True, verbose_name='Синопсис')
    notes = models.TextField(blank=True, null=True, verbose_name='Бележка')

    release_year = models.PositiveSmallIntegerField(verbose_name='Година на изданието', blank=True, null=True)

    release_number = models.PositiveSmallIntegerField(choices=BOOK_RELEASE, verbose_name='Издание', blank=True,
                                                      default=1, null=True, help_text='Поредно Издание')

    pages_count = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Брой Страници')
    measure_x = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Ширина (cм)')
    measure_y = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Височина (cм)')
    weight_grams = models.PositiveSmallIntegerField(default=250, blank=True, verbose_name='Тегло Грама')

    # TODO - a le faire en Foreign
    visual_condition = models.PositiveSmallIntegerField(choices=BOOK_CONDITION,
                                                        verbose_name='Състояние',
                                                        default=1,
                                                        null=True)

    record_created_at = models.DateTimeField(auto_now_add=True, blank=True,
                                             null=True, verbose_name='Дата на създаване на записа')
    record_updated_at = models.DateTimeField(auto_now=True, blank=True,
                                             null=True, verbose_name='Дата на промяна на записа')

    # TODO: a lier avec les wish lists
    book_to_read_by_owner = models.BooleanField(default=False, verbose_name='Непрочетена')

    price_for_rent = models.FloatField(default=1.00,
                                       verbose_name='Стойност на гаранцията (лв.)',
                                       validators=[MinValueValidator(1.0,
                                                                     message='Минималната гараранция е 1,00 лев.')])
    price_for_sell = models.FloatField(blank=True, null=True,
                                       verbose_name='Цена за продажба (лв.)',
                                       validators=[MinValueValidator(1.2, message='Минималната цена е 1,20 лева.')])

    # BOOLS
    is_hidden = models.BooleanField(default=False, verbose_name='Не показвай в Booktopia (скрита)')
    is_archived = models.BooleanField(default=False, verbose_name='Книгата е архивирана')
    is_for_sale = models.BooleanField(default=False, verbose_name='Обявена за продажба')
    is_sold = models.BooleanField(default=False, verbose_name='Книгата е продадена')
    is_lost = models.BooleanField(default=False, verbose_name='Книгата е загубена')

    # FIXME: to be removed or integrated in the general status
    book_reserved = models.BooleanField(default=False, verbose_name='Резервирана')

    # FIXME - on le update ou on le calcume selon l'histoire du truc
    has_been_rented_times = models.PositiveSmallIntegerField(blank=True, verbose_name='Заемана пъти', null=True)

    # Uploading each file in a separate file path by a pk and book name
    def file_upload_path(self, filename):
        book_id = str(self.catalog_num)
        # book_id = str(self.pk)
        return "book_images/" + book_id + "/" + filename

    cover_front = models.ImageField(upload_to=file_upload_path, verbose_name='Корица',
                                    null=True, blank=True,
                                    default='/static/generic/generic-book-2.png'
                                    # help_text="Моля, изберете снимка"
                                    )

    cover_back = models.ImageField(upload_to=file_upload_path, verbose_name='Гръб',
                                   null=True, blank=True,
                                   default='/static/generic/generic-book-2.png'
                                   # help_text="Моля, изберете снимка"
                                   )

    #
    #
    #
    #
    @property
    def cover_front_url(self):
        try:
            url = self.cover_front.url
        except:
            url = 'generic/generic-book-2.png'
        return url

    @property
    def cover_back_url(self):
        try:
            url = self.cover_back.url
        except:
            url = 'generic/generic-book-2.png'
        return url

    # FIXME: a voir comment le manque d'image joue dans l'admin
    def image_cover_front(self):
        if self.cover_front:
            return mark_safe('<img src="/media_upload/%s" width="150" height="200" />' % self.cover_front)

    def image_cover_back(self):
        if self.cover_back:
            return mark_safe('<img src="/media_upload/%s" width="150" height="200" />' % self.cover_back)

    image_cover_front.short_description = 'Преглед корица: (150*200)'
    image_cover_back.short_description = 'Преглед гръб: (150*200)'

    generated_qr_code_image = models.ImageField(upload_to=file_upload_path,
                                                verbose_name='Автоматичен QR Код', null=True,
                                                blank=True, )


    # FIXME: a le faire en readonly ou le cacher
    generated_qr_code_content = models.CharField(max_length=100, default=None,
                                                 null=True, blank=True, )
    tags = TaggableManager(blank=True,
                           verbose_name='Тагове, разделени със запетайка', )
    #
    # Foreign keys
    author_name = models.ForeignKey(Author, on_delete=models.RESTRICT,
                                    null=True, verbose_name='Автор(и)')

    # book_rent_history = models.ForeignKey(RentHistory, on_delete=models.RESTRICT,
    #                                       verbose_name='История на заеманията', blank=True, null=True)
    book_transportation_history = models.ForeignKey(StatusHistory, on_delete=models.RESTRICT,
                                                    verbose_name='История на транспортиранията', blank=True, null=True)

    # book_reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE,
    #                                  verbose_name='Ревюта', blank=True, null=True)

    # owner = models.ForeignKey(Owner, on_delete=models.RESTRICT,
    #                           verbose_name='Собственик', null=True)

    #
    # Random string generator for the QR code
    def qr_code_gen(self, request_type=None):
        cat = 'bt01'
        range_low = 1000000
        range_high = 9999999
        checksum = str(random.randint(range_low, range_high))
        chars = string.ascii_uppercase
        random_string = (''.join(random.choice(chars) for _ in range(7)))
        date_time = datetime.now()

        # https://docs.python.org/3/library/datetime.html
        if request_type == "barcode":
            # TODO: Ajouter un URL pour la suite ici (reste a savoir ou il sera loge)
            return f'{cat}|{checksum}{random_string}|{str(date_time.strftime("%a_%m_%B_%Y_%H_%M_%S")).upper()}'
        elif request_type == "checksum":
            return (cat + checksum + random_string).upper()
        else:
            return ''

    def qr_picture_gen(self, qr_code_content=None):
        qrc = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=5,
        )
        qrc.add_data(qr_code_content)
        qrc.make(fit=True)

        image = qrc.make_image(fill_color="black", back_color="white")
        image_path = str(f'{MEDIA_ROOT}/book_images/{self.catalog_num}/book_qrcode.png')
        # image_path = str(f'{MEDIA_ROOT}/book_images/{self.pk}/book_qrcode.png')
        image.save(image_path)

    def __str__(self):
        return f"{self.name} - ({self.pk})"  # {self.author_name}

    # META CLASS
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ("name",)

    # SAVE METHOD
    def save(self, *args, **kwargs):

        # Updating Checksum Field
        if not self.catalog_num:
            self.catalog_num = self.qr_code_gen("checksum")

        # Updating QR Code content
        # TODO: ADD ENCRYPTION
        if not self.generated_qr_code_content:
            self.generated_qr_code_content = self.qr_code_gen("barcode")

            # Create a pk directory if Not uploaded images
            try:
                os.mkdir(str(f'{MEDIA_ROOT}/book_images/{self.catalog_num}'))
                # os.mkdir(str(f'{MEDIA_ROOT}/book_images/{self.pk}'))
                # os.mkdir(str(f'{MEDIA_ROOT}/book_images/{self.pk}'))
            except OSError as e:
                if e.errno == 17:  # Already exists.
                    pass

            # QR Code gen and image field update
            self.qr_picture_gen(self.generated_qr_code_content)
            image_path = str(f'book_images/{self.catalog_num}/book_qrcode.png') # bez katalog num
            # image_path = str(f'book_images/{self.pk}/book_qrcode_{self.catalog_num}.png') # bez katalog num
            self.generated_qr_code_image = image_path

        # TODO: Pillow to QR - ADD id, Tag the upl image, resize, crop etc
        super(Book, self).save(*args, **kwargs)


class Comments(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

    comment = models.TextField(verbose_name='Съдържание на кометара', null=True)

    # TODO: A les sortir dans un modele ou app separee
    up_votes_count = models.PositiveSmallIntegerField(default=0)
    down_votes_count = models.PositiveSmallIntegerField(default=0)

    record_created_at = models.DateTimeField(auto_now_add=True, blank=True,
                                             null=True, verbose_name='Дата на създаване на записа')
    record_updated_at = models.DateTimeField(auto_now=True, blank=True,
                                             null=True, verbose_name='Дата на промяна на записа')

    def __str__(self):
        return f'{self.book_id}'

    class Meta:
        verbose_name = 'Коментар книга'
        verbose_name_plural = 'Коментари книги'


class CommentsAuthors(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

    comment = models.TextField(verbose_name='Съдържание на кометара', null=True)

    record_created_at = models.DateTimeField(auto_now_add=True, blank=True,
                                             null=True, verbose_name='Дата на създаване на записа')
    record_updated_at = models.DateTimeField(auto_now=True, blank=True,
                                             null=True, verbose_name='Дата на промяна на записа')

    def __str__(self):
        return f'{self.author_id}'

    class Meta:
        verbose_name = 'Коментар автор'
        verbose_name_plural = 'Коментари автори'


class CommentsEditions(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    edition_id = models.ForeignKey(Editions, on_delete=models.CASCADE)

    comment = models.TextField(verbose_name='Съдържание на кометара', null=True)

    record_created_at = models.DateTimeField(auto_now_add=True, blank=True,
                                             null=True, verbose_name='Дата на създаване на записа')
    record_updated_at = models.DateTimeField(auto_now=True, blank=True,
                                             null=True, verbose_name='Дата на промяна на записа')

    def __str__(self):
        return f'{self.edition_id}'

    class Meta:
        verbose_name = 'Коментар издателство'
        verbose_name_plural = 'Коментари издателства'


class Favourite(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, )


#
#
#
from .submodels.rent_history_model import *
from .submodels.reservations_model import *
