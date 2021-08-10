from django.core.exceptions import ValidationError, FieldError


def validate_email(value):
    if not ".com" in value:
        raise ValidationError("A valid school email must be entered in")
    else:
        return value


def validate_not_null(value):
    if len(value) == 0:
        # raise ValidationError('Това поле не може да бъде празно')
        raise FieldError('Това поле не може да бъде празно')
    else:
        return value
