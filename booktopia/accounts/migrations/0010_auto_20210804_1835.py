# Generated by Django 3.2.5 on 2021-08-04 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210720_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='egn_number',
            field=models.PositiveIntegerField(default=0, max_length=10, verbose_name='Единен граждански номер'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'МЪЖ'), ('F', 'ЖЕНА'), ('O', 'ДРУГ')], max_length=10, verbose_name='Пол'),
        ),
    ]
