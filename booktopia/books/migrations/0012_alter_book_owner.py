# Generated by Django 3.2.5 on 2021-07-28 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_owners', '0002_auto_20210720_1701'),
        ('books', '0011_auto_20210728_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='book_owners.owner', verbose_name='Собственик'),
        ),
    ]
