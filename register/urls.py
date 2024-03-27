from django.urls import path
from .views import register_user, confirm_registration

app_name = 'register'

urlpatterns = [
    path('', register_user, name='register'),
    path('confirm_registration/<str:email>/', confirm_registration, name='confirm_email'),
]