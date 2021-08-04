# Generated by Django 3.2.5 on 2021-08-04 18:01

import booktopia.books.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_owners', '0002_auto_20210720_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='Име')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('pseudonym', models.CharField(blank=True, max_length=25, null=True, unique=True, verbose_name='Псевдоним')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Рожденна Дата')),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Починал на')),
                ('nationality', models.CharField(blank=True, choices=[('AL', 'Албания'), ('DZ', 'Алжир'), ('AD', 'Андора'), ('AR', 'Аржентина'), ('AM', 'Армения'), ('AU', 'Австралия'), ('AT', 'Австрия'), ('BY', 'Беларус'), ('BE', 'Белгия'), ('BO', 'Боливия'), ('BA', 'Босна и Херцеговина'), ('BR', 'Бразилия'), ('BG', 'България'), ('KH', 'Камбоджа'), ('CM', 'Камерун'), ('CA', 'Канада'), ('IC', 'Канарски острови'), ('TD', 'Чад'), ('CL', 'Чили'), ('CN', 'Китай'), ('CO', 'Колумбия'), ('CG', 'Конго'), ('CD', 'Конго, Демократична Република'), ('CR', 'Коста Рика'), ('CI', "Кот д'Ивоар"), ('HR', 'Хърватия'), ('CY', 'Кипър'), ('CZ', 'Чехия'), ('DK', 'Дания'), ('EC', 'Египет'), ('TL', 'Еквадор'), ('EN', 'Англия'), ('ER', 'Еритрея'), ('EE', 'Естония'), ('ET', 'Етиопия'), ('FJ', 'Фиджи'), ('FI', 'Финландия'), ('FR', 'Франция'), ('GA', 'Габон'), ('GM', 'Гамбия'), ('GE', 'Грузия'), ('DE', 'Германия'), ('GH', 'Гана'), ('GI', 'Гибралтар'), ('GR', 'Гърция'), ('GD', 'Гренада'), ('GP', 'Гваделупа'), ('GY', 'Гвиана'), ('HT', 'Хаити'), ('NL', 'Холандия'), ('HK', 'Хонконг'), ('HU', 'Унгария'), ('IS', 'Исландия'), ('IN', 'Индия'), ('ID', 'Индонезия'), ('IQ', 'Ирак'), ('IL', 'Израел'), ('IT', 'Италия'), ('JM', 'Ямайка'), ('JP', 'Япония'), ('JO', 'Йордания'), ('KZ', 'Казахстан'), ('KE', 'Кения'), ('KW', 'Кувейт'), ('KG', 'Киргизстан'), ('LA', 'Лаос'), ('LV', 'Латвия'), ('LB', 'Ливан'), ('LS', 'Лесото'), ('LR', 'Либерия'), ('LI', 'Лихтенщайн'), ('LU', 'Люксембург'), ('MO', 'Макао'), ('MK', 'Северна Македония'), ('MG', 'Мадагаскар'), ('MY', 'Малайзия'), ('ML', 'Мали'), ('MT', 'Малта'), ('MQ', 'Мартиника'), ('MX', 'Мексико'), ('MD', 'Молдова'), ('MC', 'Монако'), ('MN', 'Монголия'), ('ME', 'Черна гора'), ('MA', 'Мароко'), ('MZ', 'Мозамбик'), ('NA', 'Намибия'), ('NP', 'Непал'), ('NL', 'Холандия'), ('NC', 'Нова Каледония'), ('NZ', 'НоваЗеландия'), ('NI', 'Никарагуа'), ('NE', 'Нигер'), ('NG', 'Нигерия'), ('NB', 'Северна Ирландия'), ('NO', 'Норвегия'), ('OM', 'Оман'), ('PK', 'Пакистан'), ('PA', 'Панама'), ('PG', 'Папуа Нова Гвинея'), ('PY', 'Парагвай'), ('PE', 'Перу'), ('PH', 'Филипини'), ('PL', 'Полша'), ('PT', 'Португалия'), ('PR', 'ПуертоРико'), ('QA', 'Катар'), ('CG', 'Република Конго'), ('IE', 'Република Ирландия'), ('YE', 'Република Йемен'), ('RO', 'Румъния'), ('RU', 'Русия'), ('RW', 'Руанда'), ('WS', 'Самоа'), ('SM', 'Сан Марино'), ('SA', 'Саудитска Арабия'), ('GB', 'Шотландия'), ('SN', 'Сенегал'), ('RS', 'Сърбия'), ('SG', 'Сингапур'), ('SK', 'Словакия'), ('SI', 'Словения'), ('SB', 'Соломонови острови'), ('ZA', 'Южна Африка'), ('KR', 'Южна Корея'), ('ES', 'Испания'), ('LK', 'Шри Ланка'), ('AN', 'Сен Бартелми'), ('KN', 'Сейнт Кристофър'), ('SE', 'Швеция'), ('CH', 'Швейцария'), ('PF', 'Таити'), ('TW', 'Тайван'), ('TJ', 'Таджикистан'), ('TZ', 'Танзания'), ('TH', 'Тайланд'), ('MP', 'Тиниан'), ('TG', 'Того'), ('TO', 'Тонга'), ('VG', 'Тортола'), ('TT', 'Тринидад и Тобаго'), ('TN', 'Тунис'), ('TR', 'Турция'), ('TM', 'Туркменистан'), ('UG', 'Уганда'), ('UA', 'Украйна'), ('AE', 'Обединени Арабски Емирства'), ('GB', 'Обединеното кралство'), ('US', 'САЩ'), ('UY', 'Уругвай'), ('UZ', 'Узбекистан'), ('VA', 'Ватикана'), ('VE', 'Венецуела'), ('VN', 'Виетнам'), ('GB', 'Уелс'), ('ZM', 'Замбия'), ('ZW', 'Зимбабве')], max_length=25, null=True, verbose_name='Националност')),
                ('wiki_page', models.URLField(blank=True, max_length=150, null=True, verbose_name='Страница в Уикипедиа или Биография')),
                ('record_created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата на създаване на записа')),
                ('record_updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата на промяна на записа')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Автори',
                'ordering': ('first_name', 'last_name'),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Име на книгата')),
                ('series', models.CharField(blank=True, max_length=100, null=True, verbose_name='Поредица')),
                ('translated', models.BooleanField(default=False, verbose_name='Преведена')),
                ('original_name', models.CharField(blank=True, max_length=200, verbose_name='Оригинално име')),
                ('edition_lang', models.CharField(blank=True, choices=[(1, 'Български език'), (2, 'Английски език'), (3, 'Френски език'), (4, 'Испански език'), (5, 'Немски език'), (6, 'Румънски език'), (7, 'Руски език'), (8, 'Турски език'), (9, 'Ирландски език'), (10, 'Исландски език'), (11, 'Италиански език'), (12, 'Шведски език'), (13, 'Датски език'), (14, 'Унгарски език'), (15, 'Чешки език'), (16, 'Естонски език'), (17, 'Сръбски език'), (18, 'Словашки език'), (19, 'Словенски език'), (20, 'Полски език'), (21, 'Португалски език'), (22, 'Гръцки език'), (23, 'Латински език'), (24, 'Беларуски език'), (27, 'Албански език'), (29, 'Арабски език'), (30, 'Арменски език'), (46, 'Иврит'), (57, 'Корейски език'), (60, 'Латвийски език'), (61, 'Литовски език'), (62, 'Люксембургски език'), (67, 'Малтийски език'), (72, 'Молдовски език'), (105, 'Украински език'), (110, 'Фински език'), (112, 'Хинди'), (114, 'Холандски език'), (115, 'Хърватски език'), (117, 'Японски език')], default='Български език', max_length=3, verbose_name='Език на изданието')),
                ('edition_lang_orig', models.CharField(blank=True, choices=[(1, 'Български език'), (2, 'Английски език'), (3, 'Френски език'), (4, 'Испански език'), (5, 'Немски език'), (6, 'Румънски език'), (7, 'Руски език'), (8, 'Турски език'), (9, 'Ирландски език'), (10, 'Исландски език'), (11, 'Италиански език'), (12, 'Шведски език'), (13, 'Датски език'), (14, 'Унгарски език'), (15, 'Чешки език'), (16, 'Естонски език'), (17, 'Сръбски език'), (18, 'Словашки език'), (19, 'Словенски език'), (20, 'Полски език'), (21, 'Португалски език'), (22, 'Гръцки език'), (23, 'Латински език'), (24, 'Беларуски език'), (27, 'Албански език'), (29, 'Арабски език'), (30, 'Арменски език'), (46, 'Иврит'), (57, 'Корейски език'), (60, 'Латвийски език'), (61, 'Литовски език'), (62, 'Люксембургски език'), (67, 'Малтийски език'), (72, 'Молдовски език'), (105, 'Украински език'), (110, 'Фински език'), (112, 'Хинди'), (114, 'Холандски език'), (115, 'Хърватски език'), (117, 'Японски език')], max_length=3, verbose_name='Оригинален Език')),
                ('book_current_status', models.CharField(choices=[('F', 'СВОБОДНА'), ('R', 'ЗАЕТА'), ('WR', 'ИЗЧАКВАЩА ПОЛУЧАВАНЕ ОТ ЧИТАТЕЛ'), ('WO', 'ИЗЧАКВАЩА ПОЛУЧАВАНЕ ОТ СОБСТВЕНИК'), ('S', 'ПРОДАДЕНА'), ('L', 'ЗАГУБЕНА')], default='F', max_length=25, verbose_name='Актуално състояние на книгата')),
                ('catalog_num', models.CharField(blank=True, default=None, help_text='Каталожен номер по десетична система. Полето е задължително', max_length=100, null=True, verbose_name='Вътрешен каталожен номер')),
                ('isbn_code', models.CharField(blank=True, max_length=15, null=True, verbose_name='ISBN')),
                ('oclc_code', models.CharField(blank=True, max_length=15, null=True, verbose_name='OCLC')),
                ('synopsis', models.TextField(blank=True, null=True, verbose_name='Синопсис')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Бележка')),
                ('release_year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Година на изданието')),
                ('release_number', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Първо'), (2, 'Второ'), (3, 'Трето'), (4, 'Четвърто'), (5, 'Пето'), (9, 'БЕЗ')], default=1, help_text='Поредно Издание', null=True, verbose_name='Издание')),
                ('pages_count', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Брой Страници')),
                ('measure_x', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Ширина (cм)')),
                ('measure_y', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Височина (cм)')),
                ('weight_grams', models.PositiveSmallIntegerField(blank=True, default=250, verbose_name='Тегло Грама')),
                ('visual_condition', models.PositiveSmallIntegerField(choices=[(1, 'Отлично'), (2, 'Добро'), (3, 'Лошо')], default=1, null=True, verbose_name='Състояние')),
                ('record_created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата на създаване на записа')),
                ('record_updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата на промяна на записа')),
                ('book_to_read_by_owner', models.BooleanField(default=False, verbose_name='Непрочетена')),
                ('price_for_rent', models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(1.0, message='Минималната гараранция е 1,00 лев.')], verbose_name='Стойност на гаранцията (лв.)')),
                ('price_for_sell', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1.2, message='Минималната цена е 1,20 лева.')], verbose_name='Цена за продажба (лв.)')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='Не показвай в Booktopia (скрита)')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Книгата е архивирана')),
                ('is_for_sale', models.BooleanField(default=False, verbose_name='Обявена за продажба')),
                ('is_sold', models.BooleanField(default=False, verbose_name='Книгата е продадена')),
                ('is_lost', models.BooleanField(default=False, verbose_name='Книгата е загубена')),
                ('book_reserved', models.BooleanField(default=False, verbose_name='Резервирана')),
                ('has_been_rented_times', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Заемана пъти')),
                ('cover_front', models.ImageField(blank=True, default='/static/generic/generic-book-2.png', null=True, upload_to=booktopia.books.models.Book.file_upload_path, verbose_name='Корица')),
                ('cover_back', models.ImageField(blank=True, default='/static/generic/generic-book-2.png', null=True, upload_to=booktopia.books.models.Book.file_upload_path, verbose_name='Гръб')),
                ('generated_qr_code_image', models.ImageField(blank=True, null=True, upload_to=booktopia.books.models.Book.file_upload_path, verbose_name='Автоматичен QR Код')),
                ('generated_qr_code_content', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('author_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='books.author', verbose_name='Автор(и)')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Editions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Име')),
                ('address', models.TextField(blank=True, verbose_name='Пощенски адрес')),
                ('country', models.CharField(choices=[('AL', 'Албания'), ('DZ', 'Алжир'), ('AD', 'Андора'), ('AR', 'Аржентина'), ('AM', 'Армения'), ('AU', 'Австралия'), ('AT', 'Австрия'), ('BY', 'Беларус'), ('BE', 'Белгия'), ('BO', 'Боливия'), ('BA', 'Босна и Херцеговина'), ('BR', 'Бразилия'), ('BG', 'България'), ('KH', 'Камбоджа'), ('CM', 'Камерун'), ('CA', 'Канада'), ('IC', 'Канарски острови'), ('TD', 'Чад'), ('CL', 'Чили'), ('CN', 'Китай'), ('CO', 'Колумбия'), ('CG', 'Конго'), ('CD', 'Конго, Демократична Република'), ('CR', 'Коста Рика'), ('CI', "Кот д'Ивоар"), ('HR', 'Хърватия'), ('CY', 'Кипър'), ('CZ', 'Чехия'), ('DK', 'Дания'), ('EC', 'Египет'), ('TL', 'Еквадор'), ('EN', 'Англия'), ('ER', 'Еритрея'), ('EE', 'Естония'), ('ET', 'Етиопия'), ('FJ', 'Фиджи'), ('FI', 'Финландия'), ('FR', 'Франция'), ('GA', 'Габон'), ('GM', 'Гамбия'), ('GE', 'Грузия'), ('DE', 'Германия'), ('GH', 'Гана'), ('GI', 'Гибралтар'), ('GR', 'Гърция'), ('GD', 'Гренада'), ('GP', 'Гваделупа'), ('GY', 'Гвиана'), ('HT', 'Хаити'), ('NL', 'Холандия'), ('HK', 'Хонконг'), ('HU', 'Унгария'), ('IS', 'Исландия'), ('IN', 'Индия'), ('ID', 'Индонезия'), ('IQ', 'Ирак'), ('IL', 'Израел'), ('IT', 'Италия'), ('JM', 'Ямайка'), ('JP', 'Япония'), ('JO', 'Йордания'), ('KZ', 'Казахстан'), ('KE', 'Кения'), ('KW', 'Кувейт'), ('KG', 'Киргизстан'), ('LA', 'Лаос'), ('LV', 'Латвия'), ('LB', 'Ливан'), ('LS', 'Лесото'), ('LR', 'Либерия'), ('LI', 'Лихтенщайн'), ('LU', 'Люксембург'), ('MO', 'Макао'), ('MK', 'Северна Македония'), ('MG', 'Мадагаскар'), ('MY', 'Малайзия'), ('ML', 'Мали'), ('MT', 'Малта'), ('MQ', 'Мартиника'), ('MX', 'Мексико'), ('MD', 'Молдова'), ('MC', 'Монако'), ('MN', 'Монголия'), ('ME', 'Черна гора'), ('MA', 'Мароко'), ('MZ', 'Мозамбик'), ('NA', 'Намибия'), ('NP', 'Непал'), ('NL', 'Холандия'), ('NC', 'Нова Каледония'), ('NZ', 'НоваЗеландия'), ('NI', 'Никарагуа'), ('NE', 'Нигер'), ('NG', 'Нигерия'), ('NB', 'Северна Ирландия'), ('NO', 'Норвегия'), ('OM', 'Оман'), ('PK', 'Пакистан'), ('PA', 'Панама'), ('PG', 'Папуа Нова Гвинея'), ('PY', 'Парагвай'), ('PE', 'Перу'), ('PH', 'Филипини'), ('PL', 'Полша'), ('PT', 'Португалия'), ('PR', 'ПуертоРико'), ('QA', 'Катар'), ('CG', 'Република Конго'), ('IE', 'Република Ирландия'), ('YE', 'Република Йемен'), ('RO', 'Румъния'), ('RU', 'Русия'), ('RW', 'Руанда'), ('WS', 'Самоа'), ('SM', 'Сан Марино'), ('SA', 'Саудитска Арабия'), ('GB', 'Шотландия'), ('SN', 'Сенегал'), ('RS', 'Сърбия'), ('SG', 'Сингапур'), ('SK', 'Словакия'), ('SI', 'Словения'), ('SB', 'Соломонови острови'), ('ZA', 'Южна Африка'), ('KR', 'Южна Корея'), ('ES', 'Испания'), ('LK', 'Шри Ланка'), ('AN', 'Сен Бартелми'), ('KN', 'Сейнт Кристофър'), ('SE', 'Швеция'), ('CH', 'Швейцария'), ('PF', 'Таити'), ('TW', 'Тайван'), ('TJ', 'Таджикистан'), ('TZ', 'Танзания'), ('TH', 'Тайланд'), ('MP', 'Тиниан'), ('TG', 'Того'), ('TO', 'Тонга'), ('VG', 'Тортола'), ('TT', 'Тринидад и Тобаго'), ('TN', 'Тунис'), ('TR', 'Турция'), ('TM', 'Туркменистан'), ('UG', 'Уганда'), ('UA', 'Украйна'), ('AE', 'Обединени Арабски Емирства'), ('GB', 'Обединеното кралство'), ('US', 'САЩ'), ('UY', 'Уругвай'), ('UZ', 'Узбекистан'), ('VA', 'Ватикана'), ('VE', 'Венецуела'), ('VN', 'Виетнам'), ('GB', 'Уелс'), ('ZM', 'Замбия'), ('ZW', 'Зимбабве')], max_length=100, verbose_name='Държава')),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('stars', models.PositiveSmallIntegerField(default=0, null=True)),
                ('web_address', models.URLField(blank=True, max_length=150, null=True, verbose_name='Уеб Сайт')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата на създаване на записа')),
            ],
            options={
                'verbose_name': 'Издателство',
                'verbose_name_plural': 'Издателства',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ReservationsHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата-час')),
                ('user_id', models.PositiveIntegerField()),
                ('book_id', models.PositiveIntegerField(default=0)),
                ('review', models.TextField(null=True, verbose_name='Съдържание на ревюто')),
                ('rating', models.PositiveSmallIntegerField(verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Ревю',
                'verbose_name_plural': 'Ревюта',
            },
        ),
        migrations.CreateModel(
            name='StatusHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(blank=True, null=True, verbose_name='От дата:')),
                ('rented_for_days', models.IntegerField(choices=[(7, 7), (14, 14), (21, 21), (28, 28)], default=14, verbose_name='Заета за дни:')),
                ('date_to', models.DateField(blank=True, null=True, verbose_name='До дата (авто)')),
                ('rent_event_comment', models.TextField(blank=True, null=True, verbose_name='Коментар по заемането')),
                ('degradations', models.TextField(blank=True, null=True, verbose_name='Деградации в качеството на книгата')),
                ('record_created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата на създаване на записа')),
                ('record_updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата на промяна на записа')),
                ('book_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='ID книга')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ID Потребител')),
            ],
            options={
                'verbose_name': 'История на заеманията',
                'verbose_name_plural': 'История на заеманията',
                'ordering': ('date_from',),
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True, verbose_name='Съдържание на кометара')),
                ('up_votes_count', models.PositiveSmallIntegerField(default=0)),
                ('down_votes_count', models.PositiveSmallIntegerField(default=0)),
                ('record_created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата на създаване на записа')),
                ('record_updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата на промяна на записа')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Коментар',
                'verbose_name_plural': 'Коментари',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='book_reviews',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.reviews', verbose_name='Ревюта'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_transportation_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='books.statushistory', verbose_name='История на транспортиранията'),
        ),
        migrations.AddField(
            model_name='book',
            name='editions',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='books.editions', verbose_name='Издателска къща'),
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='book_owners.owner', verbose_name='Собственик'),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Тагове, разделени със запетайка'),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Потребител'),
        ),
    ]
