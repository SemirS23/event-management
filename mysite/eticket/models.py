import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    eventID = models.IntegerField(primary_key=True),
    eventName = models.CharField(max_length=50),
    host = models.CharField(max_length=50)

class Ticket(models.Model):
    ticketID = models.IntegerField(primary_key=True),
    row = models.SmallIntegerField(),
    seatNum = models.SmallIntegerField(),
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Venue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=0)