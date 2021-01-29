from django.urls import path
from . import views as menu_views

app_name = 'menu'


urlpatterns = [
    path('piece-de-resistance/', menu_views.PrimaryMealListView.as_view(), name='primary-meals'),
    path('primary_meal/<int:pk>/', menu_views.PrimaryMealDetailView.as_view(), name='primary-meal-details'),
    path('get_primary_meals/', menu_views.PrimaryMealsListAPIView.as_view(), name='primary-meals-api'),

    path('wines/', menu_views.WineListView.as_view(), name='wines'),
    path('wine/<int:pk>/', menu_views.WineDetailView.as_view(), name='wine-details'),
    path('get_all_wines/', menu_views.WineListAPIView.as_view(), name='wines-api'),
]
