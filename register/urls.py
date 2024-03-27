from django.urls import path
from .views import register_user, confirm_registration

app_name = 'register'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('confirm/<int:user_id>/', confirm_registration, name='confirm'),
]