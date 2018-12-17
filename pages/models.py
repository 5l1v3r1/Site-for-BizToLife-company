from django.db import models

# Create your models here.
class EventTime(models.Model):
    title = models.CharField(max_length=40)
    disc = models.TextField(blank=True)
    time_to_start_event = models.DateTimeField()
