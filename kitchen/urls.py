from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    CookListView,
    DishListView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dishtypes/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "dishtypes/<int:pk>/",
        DishListView.as_view(),
        name="dish-list"
    ),
]

app_name = "kitchen"
