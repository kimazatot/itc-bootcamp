from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import model_to_dict


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        min_length=4,
        max_length=50,
        label='Имя'
    )

    last_name = forms.CharField(
        min_length=4,
        max_length=50,
        label='Фамилия'
    )

    email = forms.EmailField(
        max_length=50,
        min_length=10,
        widget=forms.EmailInput,
        label='Почта'
    )



