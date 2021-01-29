from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Order(models.Model):
    PERSONS = (
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6)
    )

    reservator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    phone = models.IntegerField(
        verbose_name='Номер Телефона'
    )

    date = models.DateField(
        verbose_name='Дата Бронирования'
    )

    time = models.TimeField(
        verbose_name='Время Бронирования'
    )

    persons = models.CharField(
        verbose_name='Количество человек',
        choices=PERSONS,
        max_length=5,
        default=PERSONS[0][0]
    )

    message = models.TextField(
        verbose_name='Комментарий',
    )

    date_created = models.DateTimeField(
        verbose_name='Дата создания Бронирования',
        default=timezone.now
    )

    def __str__(self):
        return f'{self.date} {self.time} - {self.reservator}'