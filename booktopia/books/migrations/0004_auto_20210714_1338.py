# Generated by Django 3.2.5 on 2021-07-14 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210714_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='renthistory',
            name='timestamp_from',
        ),
        migrations.RemoveField(
            model_name='transporthistory',
            name='timestamp',
        ),
    ]