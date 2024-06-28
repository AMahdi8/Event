from django.urls import path, include
from .views import upcoming_events, event


urlpatterns = [
    path('upcoming/', upcoming_events, name='upcoming_events'),
    path('upcoming/<int:pk>', event, name='event'),
]
