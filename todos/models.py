from django.db import models
from django_extensions.db.models import TimeStampedModel


class StatusChoice(models.TextChoices):
    Complete = "C", "Complete"
    Inprogress = 'I', 'Inprogress'
    Waiting = "W", "Waiting"
    Deleted = "D", "Deleted"


class Todo(TimeStampedModel):
    task = models.CharField(max_length=150)
    status = models.CharField(max_length=2, choices=StatusChoice.choices, default=StatusChoice.Waiting)