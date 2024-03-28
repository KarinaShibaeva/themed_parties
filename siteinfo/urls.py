from django.urls import path

from siteinfo.views import main_view

app_name = 'siteinfo'

urlpatterns = [
    path('main/', main_view, name='main')
]