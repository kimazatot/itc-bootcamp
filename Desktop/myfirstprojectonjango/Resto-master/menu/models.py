from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class PrimaryMeal(models.Model):
    name = models.CharField(
        verbose_name='Главное Блюдо',
        max_length=35
    )

    kitchen = models.CharField(
        verbose_name='Кухня',
        max_length=30
    )

    meal_image = models.ImageField(
        verbose_name='Фото',
        upload_to='meals'
    )

    ingredients = models.CharField(
        verbose_name='Ингредиенты',
        max_length=255
    )

    rate = models.ManyToManyField('Rate', related_name='primary_meals')

    price = models.IntegerField(
        verbose_name='Цена',
        validators=[MinValueValidator(100)]
    )

    date_created = models.DateTimeField(
        verbose_name='Дата добавления',
        default=timezone.now
    )

    def get_absolute_url(self):
        return reverse('menu:primary-meal-details', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name



class Wine(models.Model):
    CATEGORIES = (
        ('Sweet', 'Сладкое'),
        ('Half-Sweet', 'Полу-Сладкое'),
        ('Dry', 'Cухое'),
        ('Half-Dry', 'Полу-Сухое'),
    )

    COLORS = (
        ('White', 'Белое'),
        ('Red', 'Красное'),
        ('Pink', 'Розовое')
    )

    name = models.CharField(
        verbose_name='Название',
        max_length=35
    )

    wine_image = models.ImageField(
        verbose_name='Фото',
        upload_to='wines'
    )

    description = models.CharField(
        verbose_name='Описание',
        max_length=255
    )
    category = models.CharField(
        verbose_name='Категория',
        max_length=25,
        choices=CATEGORIES,
        default=CATEGORIES[0][1]
    )

    priority = models.IntegerField(
        validators=[MaxValueValidator(3)],
        verbose_name='Приоритет',
        default=None,
        blank=True
    )

    color = models.CharField(
        verbose_name='Цвет',
        max_length=10,
        choices=COLORS,
        default=COLORS[0][1]
    )

    rate = models.ManyToManyField('Rate', related_name='wines')

    price = models.IntegerField(
        verbose_name='Цена',
        validators=[MinValueValidator(100)]
    )

    date_created = models.DateTimeField(
        verbose_name='Дата добавления',
        default=timezone.now
    )

    def get_absolute_url(self):
        return reverse('menu:primary-meal-details', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name



class Rate(models.Model):
    stars = models.IntegerField(
        verbose_name='Оценка',
        validators=[MaxValueValidator(5)],
        default=0,
        unique=True
    )

    date_created = models.DateTimeField(
        verbose_name='Дата создания',
        default=timezone.now
    )

    def __str__(self) -> str:
        return f'Оценка {self.stars}'



class Breakfast(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=35
    )


    photo = models.ImageField(
        verbose_name='Фотография',
        upload_to='breakfasts'
    )


    price = models.CharField(
        verbose_name='Цена',
        max_length=35
    )


    ingredients = models.CharField(
        verbose_name='Ингредиенты',
        max_length=35
    )

    date_to_present = models.DateTimeField(
        verbose_name='Актуально до'
    )

    date_created = models.DateTimeField(
        verbose_name='Дата создания',
        default=timezone.now
    )


    def __str__(self):
        return self.name

class Lanch(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=35
    )


    photo = models.ImageField(
        verbose_name='Фотография',
        upload_to='lanches'
    )


    price = models.CharField(
        verbose_name='Цена',
        max_length=35
    )


    ingredients = models.CharField(
        verbose_name='Ингредиенты',
        max_length=35
    )

    date_to_present = models.DateTimeField(
        verbose_name='Актуально до'
    )

    date_created = models.DateTimeField(
        verbose_name='Дата создания',
        default=timezone.now
    )

    def __str__(self):
        return self.name


class Dinner(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=35
    )


    photo = models.ImageField(
        verbose_name='Фотография',
        upload_to='dinners'
    )


    price = models.CharField(
        verbose_name='Цена',
        max_length=35
    )


    ingredients = models.CharField(
        verbose_name='Ингредиенты',
        max_length=35
    )

    date_to_present = models.DateTimeField(
        verbose_name='Актуально до'
    )

    date_created = models.DateTimeField(
        verbose_name='Дата создания',
        default=timezone.now
    )

    def __str__(self):
        return self.name

