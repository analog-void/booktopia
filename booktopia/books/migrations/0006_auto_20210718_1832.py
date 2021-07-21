# Generated by Django 3.2.5 on 2021-07-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_is_for_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_archived',
            field=models.BooleanField(default=False, verbose_name='Книгата е архивирана'),
        ),
        migrations.AddField(
            model_name='book',
            name='is_lost',
            field=models.BooleanField(default=False, verbose_name='Книгата е загубена'),
        ),
        migrations.AddField(
            model_name='book',
            name='is_sold',
            field=models.BooleanField(default=False, verbose_name='Книгата е продадена'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_current_status',
            field=models.CharField(choices=[('F', 'СВОБОДНА'), ('R', 'ЗАЕТА'), ('WR', 'ИЗЧАКВАЩА ПОЛУЧАВАНЕ ОТ ЧИТАТЕЛ'), ('WO', 'ИЗЧАКВАЩА ПОЛУЧАВАНЕ ОТ СОБСТВЕНИК'), ('S', 'ПРОДАДЕНА'), ('BR', 'БРАКУВАНА'), ('L', 'ЗАГУБЕНА')], default='F', max_length=25, verbose_name='Актуално състояние на книгата'),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_hidden',
            field=models.BooleanField(default=False, verbose_name='Не показвай в Booktopia'),
        ),
    ]
