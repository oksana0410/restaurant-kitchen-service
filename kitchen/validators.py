from django.core.exceptions import ValidationError


def validate_year_of_experience(year_of_experience):
    if year_of_experience < 0:
        raise ValidationError(
            "Amount of years experience can not be negative!"
        )
    if year_of_experience > 100:
        raise ValidationError(
            "Amount of years experience can not be more than 100!"
        )

    return year_of_experience


def validate_price(price):
    if price < 0:
        raise ValidationError(
            "Price can not be negative!"
        )

    return price
