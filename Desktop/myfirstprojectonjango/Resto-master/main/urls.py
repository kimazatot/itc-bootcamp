from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('api/v1/get_all_users/', views.UserListAPIView.as_view(), name='get-all-users-api'),
    path('api/v1/update_user/', views.UserUpdateAPIView.as_view(), name='create-users-api'),

    path('api/v1/get_all_feedbacks/', views.FeedbackListAPIView.as_view(), name='get-all-feedbacks-api'),
    path('api/v1/create_feedback/', views.FeedbackCreateAPIView.as_view(), name='create-feedback-api'),
    path('api/v1/update_feedback/', views.FeedbackUpdateAPIView.as_view(), name='update-feedback-api'),
    path('api/v1/delete_feedback/', views.FeedbackDeleteView.as_view(), name='delete-feedback-api'),

    path('api/v1/get_all_comments/', views.CommentListAPIView.as_view(), name='get-all-comments-api'),
    path('api/v1/create_comment/', views.CommentListAPIView.as_view(), name='update-comment-api'),
    path('api/v1/update_comment/', views.UserDetailsAPIView.as_view(), name='update-comment-api'),
    path('api/v1/delete_comment/', views.UserDetailsAPIView.as_view(), name='delete-comment-api'),
    
]
