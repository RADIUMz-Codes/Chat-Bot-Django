from django.contrib import admin
from .models import Incident, IncidentTypes

# Register your models here.
admin.site.register(Incident)
admin.site.register(IncidentTypes)
