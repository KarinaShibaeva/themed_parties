from django.urls import path
from .views import register, confirm_email

app_name = 'register'

urlpatterns = [
    path('', register, name='register'),
    path('confirm_email/<str:email>/', confirm_email, name='confirm_email'),
]