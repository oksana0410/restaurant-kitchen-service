from django.contrib.auth import get_user_model
from django.test import TestCase

from django.urls import reverse

from kitchen.models import DishType, Dish

DISHES_URL = reverse("kitchen:dish-list")
COOKS_URL = reverse("kitchen:cook-list")
DISH_TYPES_URL = reverse("kitchen:dish-type-list")


class PublicViewTest(TestCase):
    def test_dish_login_required(self):
        res = self.client.get(DISHES_URL)

        self.assertNotEqual(res.status_code, 200)

    def test_cook_login_required(self):
        res = self.client.get(COOKS_URL)

        self.assertNotEqual(res.status_code, 200)

    def test_dish_type_login_required(self):
        res = self.client.get(DISH_TYPES_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test_password"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="test_name1")
        DishType.objects.create(name="test_name2")

        response = self.client.get(DISH_TYPES_URL)
        dish_types = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

    def test_retrieve_dish(self):
        dish_type = DishType.objects.create(name="test_name")
        Dish.objects.create(
            name="test_name_1",
            dish_type=dish_type,
            price=2
        )
        Dish.objects.create(
            name="test_name_2",
            dish_type=dish_type,
            price=2
        )

        response = self.client.get(DISHES_URL)
        dishes = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(response, "kitchen/dish_list.html")
