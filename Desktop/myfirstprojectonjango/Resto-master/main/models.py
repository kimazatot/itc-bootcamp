from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    user_profile_photo = models.ImageField(
        upload_to='user_profiles',
        verbose_name='Фото профиля',
        default='anonym_author.png'
    )

    def __str__(self):
        return f'Профиль пользователя {self.user.first_name} {self.user.last_name}'


class Feedback(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор Отзыва'
    )

    feedback_text = models.TextField(
        verbose_name='Оставьте Отзыв'
    )

    date_created = models.DateTimeField(
        verbose_name='Дата создания отзыва',
        default=timezone.now
    )

    def get_absolute_url(self):
        return reverse('feedback-details', kwargs={'pk':self.pk})

    def __str__(self):
        return f'{self.feedback_text}'


class Comment(models.Model):
    '''Данная модель создаёт объект комментария в привязанного к отзыву.'''
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария'
    )

    assigned_to_feedback = models.ForeignKey(
        Feedback,
        on_delete=models.CASCADE,
        verbose_name='Отзыв',
        related_name='comments'
    )

    comment_text = models.TextField(
        verbose_name='Текст Комментария'
    )

    date_created = models.DateTimeField(
        verbose_name='Дата создания комментария',
        default=timezone.now)

    def __str__(self):
        return f'Комментарий {self.assigned_to_feedback}'

