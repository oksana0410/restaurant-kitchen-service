from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import DishType, Dish, Cook
from kitchen.validators import validate_price, validate_year_of_experience


class CookForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = ["username", "first_name", "last_name", "years_of_experience"]

    def clean_years_of_experience(self) -> str:
        years_of_experience = self.cleaned_data["years_of_experience"]

        return validate_year_of_experience(years_of_experience)


class CookUpdateForm(forms.ModelForm):
    dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Cook
        fields = ["first_name", "last_name", "years_of_experience"]

    def clean_years_of_experience(self) -> str:
        years_of_experience = self.cleaned_data["years_of_experience"]

        return validate_year_of_experience(years_of_experience)


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]

    def clean_price(self) -> str:
        price = self.cleaned_data["price"]

        return validate_price(price)


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )
