from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User


class TeamMember(models.Model):
    EDUCATIONS = (
        ('Bachelor', 'Бакалавр'),
        ('College', 'Техникум или Коледж'),
        ('Self-Educated', 'Самоучка')
    )

    POSITIONS = (
        ('Генеральный Директор', 'Генеральный Директор'),
        ('Шеф Повар', 'Шеф Повар'),
        ('Повар', 'Повар'),
        ('Стажёр', 'Стажёр')
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='team_members'
    )


    position = models.CharField(
        verbose_name='Должность',
        max_length=25,
        choices=POSITIONS,
        default=POSITIONS[-1][0]
    )

    education = models.CharField(
        verbose_name='Образование',
        max_length=30,
        choices=EDUCATIONS,
        default=EDUCATIONS[0][0]
    )

    experience = models.IntegerField(
        verbose_name='Реальный стаж работы'
    )

    companies = models.CharField(
        verbose_name='История Работы',
        max_length=255
    )

    date_registered = models.DateTimeField(
        verbose_name='Дата регистрации',
        default=timezone.now
    )

    def get_absolute_url(self):
        return reverse('teams:member-details', kwrags={'pk':self.pk})

    def __str__(self):
        return f'{self.position} - {self.user.first_name} {self.user.last_name}'