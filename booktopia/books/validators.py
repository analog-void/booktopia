from django.core.exceptions import ValidationError

from .models import Book


# Price validators
def validate_sell_price(rent_price):
    if Book.price_for_sell < rent_price * 1.2:
        raise ValidationError('Обявената продажна цена трябва да е поне 20% по-висока от стойността на гаранцията')


def validate_rent_price(sell_price):
    if sell_price:
        if Book.price_for_rent > sell_price * 0.8:
            raise ValidationError('Обявената продажна цена трябва да е поне 20% по-висока от стойността на гаранцията')


def validate_min_rent(rent_price):
    if rent_price < 1:
        raise ValidationError('Минималната стойност на гаранцията е 1 (един) лев.')


def validate_min_sell(sell_price):
    if sell_price < 1:
        raise ValidationError('Минималната стойност на продажната цена е 1,20 лева.')


