from django.urls import path

from appeal.views import submit_appeal

app_name = 'appeal'

urlpatterns = [
    path('<int:event_id>/appeal', submit_appeal, name='appeals')
]