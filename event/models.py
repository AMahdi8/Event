from django.db import models
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()

    def is_past(self):
        return self.date > timezone.now()

    def __str__(self) -> str:
        return self.name
