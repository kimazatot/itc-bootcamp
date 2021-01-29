from django import forms
from .models import Order

PERSONS = [
    ("ONE", 1),
    ("TWO", 2),
    ("THREE", 3),
    ("FOUR", 4),
    ("FIVE", 5),
    ("SIX", 6)
]

class ReservationForm(forms.ModelForm):
     class Meta:
        model = Order
        fields = '__all__'
        exclude = ['reservator', 'date_created']
        widgets = {
                'message': forms.Textarea(
                    attrs={
                        'cols': 35, 
                        'rows': 3
                    }
                ),
                'date': forms.DateInput(
                    attrs={
                        'class': 'form-control datetimepicker-input',
                        'data-target': '#datetimepicker4',
                        'placeholder':'Date'
                    }
                ),
                'time': forms.DateInput(
                    attrs=
                    {
                        'class': 'form-control timepicker-input',
                        'data-target': '#datetimepicker3',
                        'placeholder':'Time',
                        'type': 'time'
                    }
                ),
                'persons': forms.Select(
                    attrs={
                        'class':'form-control',
                        'id':'selectPerson'
                    }
                )
        }
