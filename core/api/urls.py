from home.views import index
from django.urls import path
from incident.views import incident, incident_types

urlpatterns = [
    path('index/', index),
    path('incident/',incident),
    path('incident-types/', incident_types),
]