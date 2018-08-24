from enum import IntEnum

from django.db import models
from django.db.models import fields
# Create your models here.

class Meal(IntEnum):
    LUNCH = 1
    DINNER = 2


class MealPlan(models.Model):
    LUNCH_CHOICES = tuple(
        # e.g. (1, "Lunch")
        (m.value, m.name.title())
        for m in  Meal
    )

    date = fields.DateField(db_index=True)
    recipe_name = fields.CharField(max_length=255)
    meal_id = fields.IntegerField(choices=LUNCH_CHOICES)
