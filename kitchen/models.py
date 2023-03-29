from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True)
    kitchen_process = models.ManyToManyField(KitchenProcess, related_name="cooks")

    class Meta:
        ordering = ["username"]
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self) -> str:
        return (f"Username: {self.username} "
                f"Name: {self.first_name} "
                f"Surname: {self.last_name})"
                )


class KitchenProcess(models.Model):
    process = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Process: {self.process}"


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Dish type: {self.name}"



