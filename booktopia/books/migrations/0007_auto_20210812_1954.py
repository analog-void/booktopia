# Generated by Django 3.2.5 on 2021-08-12 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0006_auto_20210810_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Коментар книга', 'verbose_name_plural': 'Коментари книги'},
        ),
        migrations.CreateModel(
            name='CommentsEditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True, verbose_name='Съдържание на кометара')),
                ('record_created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата на създаване на записа')),
                ('record_updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата на промяна на записа')),
                ('edition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.editions')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Коментар издателство',
                'verbose_name_plural': 'Коментари издателства',
            },
        ),
        migrations.CreateModel(
            name='CommentsAuthors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True, verbose_name='Съдържание на кометара')),
                ('record_created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата на създаване на записа')),
                ('record_updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата на промяна на записа')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Коментар автор',
                'verbose_name_plural': 'Коментари автори',
            },
        ),
    ]
