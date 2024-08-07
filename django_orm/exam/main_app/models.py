from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator
from django.db import models
from django.db.models import Count


class AstronautManager(models.Manager):
    def get_astronauts_by_missions_count(self):
        return self.annotate(missions_count=Count('missions')).order_by('-missions_count', 'phone_number')


class BaseModel(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class Astronaut(BaseModel):
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\d+$')],
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    spacewalks = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    objects = AstronautManager()


class Spacecraft(BaseModel):
    manufacturer = models.CharField(
        max_length=100,
    )

    capacity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    weight = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )

    launch_date = models.DateField()


class Mission(BaseModel):
    STATUSES = [
        ("Planned", "Planned"),
        ("Ongoing", "Ongoing"),
        ("Completed", "Completed"),
    ]

    description = models.TextField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        choices=STATUSES,
        max_length=9,
        default='Planned'
    )

    launch_date = models.DateField()

    spacecraft = models.ForeignKey(
        Spacecraft,
        on_delete=models.CASCADE,
        related_name='spacecrafts_usage'
    )

    astronauts = models.ManyToManyField(
        Astronaut,
        related_name='missions'
    )

    commander = models.ForeignKey(
        Astronaut,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='commanded_missions',
    )
