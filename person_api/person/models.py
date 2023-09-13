from django.core.exceptions import ValidationError
from django.db import models

def validate_string(value):
    if not isinstance(value, str):
        raise ValidationError("Name must be a string.")

class Person(models.Model):
    name = models.CharField(max_length=100, validators=[validate_string])
    # Other fields in your Person model

    def __str__(self):
        return self.name
