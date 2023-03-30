from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookForm, DishForm, DishTypeForm
from kitchen.models import Cook, Dish, DishType


def index(request):
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 5


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy('kitchen:dish-type-list')


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy('kitchen:dish-type-list')


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy('kitchen:dish-type-list')


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
