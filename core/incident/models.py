from django.db import models


class IncidentTypes(models.Model):
    inc_type = models.CharField(max_length=30)

    def __str__(self):
        return self.inc_type
    
    
class Incident(models.Model):
    incident_type = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    

