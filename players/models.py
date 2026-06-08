from django.db import models

# Create your models here.


class Sport(models.Model):
    name = models.CharField(max_length=255, unique=True)


class PlayerProfile(models.Model):
    GENDER_MALE = "M"
    GENDER_FEMALE = "F"

    GENDER_CHOICES = [(GENDER_MALE, "Male"), (GENDER_FEMALE, "Female")]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    primary_position = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height_cm = models.PositiveIntegerField()
    weight_kg = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    sports = models.ForeignKey(Sport, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
