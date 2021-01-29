from django.contrib import admin
from .models import Feedback, Comment, UserProfile

admin.site.register(Feedback)
admin.site.register(Comment)
admin.site.register(UserProfile)