from django.core import validators, exceptions
from django.db import models

# Create your models here.

def validate_string_min_len(value, min_len):
    if value < min_len :
        raise exceptions.ValidationError(f"The username must be a minimum of {min_len} chars")


class Profile(models.Model):
    MIN_USERNAME_LENGT = 2
    MAX_USERNAME_LENGT = 10
    MIN_AGE_VALUE = 18
    MAX_PASSWORD_LENGT = 30
    MAX_FIRST_NAME_LENGT = 30
    MAX_LAST_NAME_LENGT = 30
    MESSAGE_USERNAME_MIN_LENGT = f"The username must be a minimum of {MIN_USERNAME_LENGT} chars"


    username = models.CharField(
        max_length=MAX_USERNAME_LENGT,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(MIN_USERNAME_LENGT, message=MESSAGE_USERNAME_MIN_LENGT),
            # validate_string_min_len,
        ]
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[
            validators.MinValueValidator(MIN_AGE_VALUE),
        ]
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGT,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGT,
        null=True,
        blank=True,

    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGT,
        null=True,
        blank=True,

    )

    profile_picture = models.URLField()

class Car(models.Model):
    MAX_TYPES_CAR_LENGTH = 10
    MAX_MODEL_LENGT = 20
    MIN_MODEL_LENGT = 2
    MIN_YEAR_VALUE = 1980
    MAX_YEAR_VALUE = 2049

    MESSAGE_AGE_MIN_VALUE = f'Year must be between {MIN_YEAR_VALUE} and {MAX_YEAR_VALUE}'

    SPORT_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER_CAR = "Other"

    CARS_TYPES = [
        (SPORT_CAR, SPORT_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER_CAR, OTHER_CAR),
    ]

    my_type = models.CharField(
        max_length=MAX_TYPES_CAR_LENGTH,
        choices=CARS_TYPES,
        null=False,
        blank=False,

    )

    my_model = models.CharField(
        max_length=MAX_MODEL_LENGT,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(MIN_MODEL_LENGT),
         ]
    )

    year = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[
            validators.MinValueValidator(MIN_YEAR_VALUE, message= MESSAGE_AGE_MIN_VALUE),
        ]

    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(1),
        )
    )
