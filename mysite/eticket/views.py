from django.shortcuts import redirect, render
from .models import Venue, Event, Ticket

# Create your views here.
def home(request):
    context = {}
    return render(request, "eticket/home.html", context)

def venue(request):
    venues = Venue.objects.all()
    if request.method == 'POST':
        venue_name = request.POST.get('name')
        location = request.POST.get('location')
        capacity = request.POST.get('capacity')
        Venue.objects.create(
            name=venue_name, 
            location=location, 
            capacity=capacity, 
            owner=request.user
        )
        return redirect('eticket:venue')
    context = {'venues':venues}
    return render(request, "eticket/venue.html", context)


def hostEvent(request):
    events = Event.objects.all()
    venues = Venue.objects.all()
    if request.method == 'POST':
        event_name = request.POST.get('eventName')
        venue_id = request.POST.get('venue')
        venue = Venue.objects.get(pk=venue_id)
        price = request.POST.get('ticketPrice')
        Event.objects.create(
            eventName=event_name,
            host=request.user,
            venue=venue,
            ticketPrice = price,
            ticketQuantity = venue.capacity,
        )
        return redirect('eticket:event')
    context = {'events':events, 'venues':venues}
    return render(request, "eticket/hostEvent.html", context)

def buyTickets(request):
    tickets = Ticket.objects.all()
    events = Event.objects.all()
    if request.method == 'POST':
        row = int(request.POST.get('row'))
        print(row)
        seat_num = int(request.POST.get('seatNum'))
        print(seat_num)
        event_id = request.POST.get('event')
        event = Event.objects.get(pk=event_id)
        quantity = request.POST.get('quantity') 
        event.ticketQuantity -= int(quantity)
        event.save()
        Ticket.objects.create(
            row=row, 
            seatNum = seat_num,
            event=event
        )
        return redirect('eticket:ticket')
    context = {'tickets':tickets, 'events':events}
    return render(request, "eticket/buyTicket.html", context)

