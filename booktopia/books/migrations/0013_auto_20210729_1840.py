# Generated by Django 3.2.5 on 2021-07-29 18:40

import booktopia.books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_alter_book_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_back',
            field=models.ImageField(blank=True, null=True, upload_to=booktopia.books.models.Book.file_upload_path, verbose_name='Гръб'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_front',
            field=models.ImageField(blank=True, null=True, upload_to=booktopia.books.models.Book.file_upload_path, verbose_name='Корица'),
        ),
        migrations.AlterField(
            model_name='book',
            name='edition_lang',
            field=models.CharField(blank=True, choices=[(1, 'Български език'), (2, 'Английски език'), (3, 'Френски език'), (4, 'Испански език'), (5, 'Немски език'), (6, 'Румънски език'), (7, 'Руски език'), (8, 'Турски език'), (9, 'Ирландски език'), (10, 'Исландски език'), (11, 'Италиански език'), (12, 'Шведски език'), (13, 'Датски език'), (14, 'Унгарски език'), (15, 'Чешки език'), (16, 'Естонски език'), (17, 'Сръбски език'), (18, 'Словашки език'), (19, 'Словенски език'), (20, 'Полски език'), (21, 'Португалски език'), (22, 'Гръцки език'), (23, 'Латински език'), (24, 'Беларуски език'), (27, 'Албански език'), (29, 'Арабски език'), (30, 'Арменски език'), (46, 'Иврит'), (57, 'Корейски език'), (60, 'Латвийски език'), (61, 'Литовски език'), (62, 'Люксембургски език'), (67, 'Малтийски език'), (72, 'Молдовски език'), (105, 'Украински език'), (110, 'Фински език'), (112, 'Хинди'), (114, 'Холандски език'), (115, 'Хърватски език'), (117, 'Японски език')], default='Български език', max_length=3, verbose_name='Език на изданието'),
        ),
    ]