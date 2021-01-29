from django.db.models import fields
from .models import UserProfile, Feedback, Comment
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.relations import SlugRelatedField

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined"
        )


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='first_name', read_only=True)
    assigned_to_feedback = SlugRelatedField(slug_field='feedback_text', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='first_name', read_only=True)

    comments = CommentSerializer(many=True, required=False)
    class Meta:
        model = Feedback
        fields = (
            'author',
            'feedback_text',
            'comments',
            'date_created'
        )
