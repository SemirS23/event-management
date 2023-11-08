from django.db import models

# Create your models here.
class Event(models.Model):
    eventID = models.IntegerField(primary_key=True),
    eventName = models.CharField(max_length=50),
    host = models.CharField(max_length=50)

class Ticket(models.Model):
    ticketID = models.IntegerField(primary_key=True),
    row = models.SmallIntegerField(),
    seatNum = models.SmallIntegerField(),
    price = models.DecimalField()

class Venue(models.Model):
    venueID = models.IntegerField(primary_key=True),
    venueName = models.CharField(max_length=50),
    location = models.CharField(max_length=30),
    capacity = models.SmallIntegerField()

class Account(models.Model):
    accountID = models.IntegerField(primary_key=True),
    ticketID = models.ForeignKey(Ticket, default=None),
    eventID = models.ForeignKey(Event, default=None)