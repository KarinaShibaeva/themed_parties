from django.urls import path
from .views import register_user, activate

app_name = 'register'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('activate/<str:token>/', activate, name='activate'),
]