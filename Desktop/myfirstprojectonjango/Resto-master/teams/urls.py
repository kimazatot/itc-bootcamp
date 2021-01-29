from django.contrib.auth import default_app_config
from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.TeamMemberCreateView.as_view(), name='all-team'),
    path('details/<int:pk>/', views.TeamMemberDetailView.as_view(), name='member-details')
]
