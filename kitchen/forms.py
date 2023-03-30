from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import DishType, Dish, Cook


class CookForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = ["username", "first_name", "last_name", "years_of_experience"]
