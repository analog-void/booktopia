# Generated by Django 3.2.5 on 2021-07-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=25, verbose_name='Име'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=25, verbose_name='Фамилия'),
        ),
    ]