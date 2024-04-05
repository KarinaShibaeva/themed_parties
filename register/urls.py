from django.urls import path

from register.views import register_user, confirm_account, registration_success, login_user, profile, logout_user, \
    delete_booking

app_name = 'register'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('confirm/<str:confirmation_code>/', confirm_account, name='confirm_account'),
    path('registration_success/', registration_success, name='registration_success'),
    path('login/', login_user, name='login'),
    path('profile/', profile, name='profile'),
    path('delete_booking/<int:booking_id>/', delete_booking, name='delete_booking'),
    path('logout/', logout_user, name='logout'),
]