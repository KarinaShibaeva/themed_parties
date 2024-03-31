from django.urls import path

from register.views import register_user

app_name = 'register'

urlpatterns = [
    path('register/',register_user, name='register'),
]