from django.db import models

class vic_event(models.Model):  # Corrected superclass name
    event_name = models.CharField(max_length=100)
    event_date = models.CharField(max_length=100)
    event_time = models.CharField(max_length=100)
    event_location = models.CharField(max_length=100)
    event_description = models.TextField()
    guests=models.CharField(max_length=100,default='')
    event_category = models.CharField(max_length=100)
