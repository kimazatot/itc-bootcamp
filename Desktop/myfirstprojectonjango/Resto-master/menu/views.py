import datetime as dt
from rest_framework import generics
from rest_framework.views import APIView
from django.views.generic import ListView, DetailView
from .models import Breakfast, PrimaryMeal, Wine, Lanch, Dinner


class PrimaryMealListView(ListView):
    model = PrimaryMeal
    template_name = 'menu/primary_meals.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        start = dt.datetime.strftime(dt.datetime.today() - dt.timedelta(days=1), '%Y-%m-%d')
        end = dt.datetime.strftime(dt.datetime.today() + dt.timedelta(days=365), '%Y-%m-%d')
        kwargs["breakfasts"] = Breakfast.objects.filter(date_to_present__range=[start, end])
        kwargs["lanches"] = Lanch.objects.filter(date_to_present__range=[start, end])
        kwargs["dinners"] = Dinner.objects.filter(date_to_present__range=[start, end])
        return super().get_context_data(**kwargs)


class PrimaryMealDetailView(DetailView):
    model = PrimaryMeal
    template_name = 'menu/primary_details.html'


class PrimaryMealsListAPIView(APIView):
    def get(self, request):
        pass



class WineListView(ListView):
    model = Wine
    template_name = 'menu/wines.html'

    def get_context_data(self, **kwargs):
        kwargs["wines_first_priority"] = Wine.objects.filter(priority__range=[1, 2])
        kwargs["wines_other_priority"] = Wine.objects.filter(priority__range=[3, 10])
        return super().get_context_data(**kwargs)


class WineDetailView(DetailView):
    model = Wine
    template_name = 'menu/wine_details.html'
    context_object_name = 'object'


class WineListAPIView(generics.ListAPIView):
    def get(self, request):
        pass



