import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
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

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    eventName = models.CharField(max_length=50, default="")
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True)
    ticketPrice = models.DecimalField(max_digits=10, decimal_places=2, default=50)