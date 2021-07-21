from django.db import models

from booktopia.common.general_choices import BOOK_RUNNER_STATUS, BOOK_RUNNER_DELIVERY_RATING


class RunnerCompany(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Име на Компанията')
    email = models.EmailField(max_length=50, unique=True,
                              verbose_name='Имейл Адрес')
    phone_1 = models.CharField(max_length=20, default='+359 8',
                               verbose_name='Основен Телефон за Контакт')
    phone_2 = models.CharField(max_length=20, null=True, blank=True,
                               verbose_name='Допълнителен телефон за контакт')

    cover_back = models.ImageField(upload_to='runners_images/', verbose_name='Лого на компанията',
                                   null=True, blank=True, help_text="Моля, изберете снимка")

    # company rating - on le trouve ou?

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class RunnerLog(models.Model):
    transportation_type = models.PositiveSmallIntegerField(choices=BOOK_RUNNER_STATUS,
                                                           verbose_name='Тип транспорт')
    runner_id = models.ForeignKey(RunnerCompany, on_delete=models.CASCADE, verbose_name='Име на компанията')
    from_place = models.CharField(max_length=100, verbose_name='от позиция')
    to_place = models.CharField(max_length=100, verbose_name='до позиция')

    ts_pickup = models.DateTimeField(null=True, verbose_name='Дата / час')
    ts_delivery = models.DateTimeField(null=True, verbose_name='Дата / час')

    delivery_rating = models.PositiveSmallIntegerField(default=5, verbose_name='Рейтинг на поръчката',
                                                       choices=BOOK_RUNNER_DELIVERY_RATING)
    comment = models.TextField(verbose_name='Коментар', null=True, blank=True)

    # FIXME: a le cheker
    def calculated_rating(self):
        num_events = RunnerLog.objects.count()
        sum_ratings = [int(self.delivery_rating) for self.delivery_rating in RunnerLog.objects.all()]
        return f'{num_events} | {sum_ratings}'

    def __str__(self):
        return f'{self.from_place} => {self.to_place} на {self.ts_pickup}'

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'
