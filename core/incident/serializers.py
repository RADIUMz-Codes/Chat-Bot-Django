from rest_framework import serializers
from .models import Incident, IncidentTypes

class IncidentTypeSerializer (serializers.ModelSerializer):
    class Meta:
        model = IncidentTypes
        fields = ['id', 'inc_type']
        

class IncidentSerializer (serializers.ModelSerializer):

    class Meta:
        model = Incident
        fields = ['id','incident_type','description']
        