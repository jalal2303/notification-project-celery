from django.urls import path
from .views import send_notification

urlpatterns = [
    path("<str:project>/notify/", send_notification),
]