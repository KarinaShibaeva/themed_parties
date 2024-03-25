from django.urls import path

from appeal.views import submit_appeal

app_name = 'appeal'

urlpatterns = [
    path('', submit_appeal, name='appeals')
]