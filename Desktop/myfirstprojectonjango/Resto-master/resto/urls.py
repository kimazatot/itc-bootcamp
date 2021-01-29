from django.contrib import admin
from django.conf import settings
from main import views as main_views
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('register/', main_views.registration, name='registration-page'),
    path('reservation/', include('reservation.urls'), name='reservation'),

    path('', include('main.urls')),
    path('teams/', include('teams.urls')),
    path('menu/', include('menu.urls')),

    # path('change_profile/', main_views.change_profile, name='change_profile'),
    path('feedbacks/', main_views.FeedbackListView.as_view(), name='all_feedbacks'),
    path('feedback/<int:pk>/', main_views.FeedbackDetailView.as_view(), name='feedback-details'),
    path('feedback/create/', main_views.FeedbackCreateView.as_view(), name='feedback-create'),
    path('feedback/update/<int:pk>/', main_views.FeedbackUpdateView.as_view(), name='feedback-update'),
    path('feedback/delete/<int:pk>/', main_views.FeedbackDeleteView.as_view(), name='feedback-delete'),
    path('api-auth/', include('rest_framework.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)