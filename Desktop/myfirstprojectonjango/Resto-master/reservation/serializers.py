from django.db.models.fields import SlugField
from rest_framework import serializers
from reservation import models

class OrderSerializer(serializers.ModelSerializer):
    reservator = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = models.Order
        exclude = ['date_created',]

