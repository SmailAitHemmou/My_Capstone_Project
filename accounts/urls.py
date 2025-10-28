from django.urls import path
from .views import CustomLoginView, RegisterView
from django.contrib.auth.views import LogoutView
from . import api_views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api/users/', api_views.UserListAPIView.as_view(), name='api-users'),
]