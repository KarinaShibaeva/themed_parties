from django.urls import path

from register.views import register_user, confirm_account

app_name = 'register'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('confirm/<str:confirmation_code>/', confirm_account, name='confirm_account'),
]