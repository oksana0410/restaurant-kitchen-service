from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class KitchenProcess(models.Model):
    process = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Process: {self.process}"


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True)
    kitchen_process = models.ManyToManyField(KitchenProcess, prefetch_related="cooks")

    class Meta:
        ordering = ["username"]
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self) -> str:
        return (
            f"Username: {self.username} "
            f"Name: {self.first_name} "
            f"Surname: {self.last_name})"
        )


class DishType(models.Model):
    name = models.CharField(max_length=255)
    kitchen_process = models.ForeignKey(KitchenProcess, on_delete=models.CASCADE)

    def __str__(self):
        return f"Dish type: {self.name}"


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, prefetch_related="dishes")

    class Meta:
        ordering = ["id"]
        verbose_name = "dish"
        verbose_name_plural = "dishes"

    def __str__(self) -> str:
        return f"Name: {self.name}"
