from django.urls import path
from .views import RegisterUserView, ConfirmEmailView

app_name = 'register'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('activate/<str:token>/', ConfirmEmailView.as_view(), name='activate'),
]