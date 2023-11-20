from django.contrib import admin
from .models import Venue, Event, Ticket
# Register your models here.
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Ticket)