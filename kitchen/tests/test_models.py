from django.test import TestCase

from django.contrib.auth import get_user_model

from kitchen.models import Dish, DishType


class ModelsTests(TestCase):
    def test_dish_str(self):
        dish_type = DishType.objects.create(name="TestName")
        dish = Dish.objects.create(
            name="test_name", dish_type=dish_type, price=2.00
        )

        self.assertEqual(str(dish), dish.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="test_username",
            first_name="test_first_name",
            last_name="test_last_name",
        )

        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="TestName")
        self.assertEqual(str(dish_type), dish_type.name)
