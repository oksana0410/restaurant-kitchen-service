from django.test import TestCase
from django.contrib.auth import get_user_model

from kitchen.forms import CookForm
from kitchen.models import Dish, DishType


class FormsTest(TestCase):
    def test_cook_form_with_years_of_experience_first_last_name_is_valid(self):
        form_data = {
            "username": "test_username",
            "password1": "test_password",
            "password2": "test_password",
            "years_of_experience": 5,
            "first_name": "test_first_name",
            "last_name": "test_last_name"
        }
        form = CookForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class SearchFormTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test_password"
        )
        self.client.force_login(self.user)

    def test_cook_search(self):
        search_request = "test_search"
        response = self.client.get(f"/cooks/?username={search_request}")

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["cook_list"],
            get_user_model().objects.filter(username__icontains=search_request)
        )

    def test_dish_search(self):
        search_request = "test_search"
        response = self.client.get(f"/dishes/?name={search_request}")

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["dish_list"],
            Dish.objects.filter(name__icontains=search_request)
        )

    def test_dish_type_search(self):
        search_request = "test_search"
        response = self.client.get(f"/dish-types/?name={search_request}")

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["dish_type_list"],
            DishType.objects.filter(name__icontains=search_request)
        )
