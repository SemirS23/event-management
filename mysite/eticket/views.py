from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Venue, Event, Ticket
from users.models import Account
from django.contrib.auth.models import User

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
    tickets = Ticket.objects.filter(ticketHolder=request.user)
    account = Account.objects.get(user=request.user)
    events = Event.objects.all()
    if request.method == 'POST':
        row = int(request.POST.get('row'))
        seat_num = int(request.POST.get('seatNum'))
        event_id = request.POST.get('event')
        event = Event.objects.get(pk=event_id)
        quantity = request.POST.get('quantity') 
        event.ticketQuantity -= int(quantity)
        event.save()
        price = int(quantity) * event.ticketPrice
        account.balance -= price
        account.save() 
        for i in range(int(quantity)):
            Ticket.objects.create(
                row=row, 
                seatNum = seat_num,
                event=event,
                ticketHolder=request.user
            )
        return redirect('eticket:ticket')
    context = {'tickets':tickets, 'events':events}
    return render(request, "eticket/buyTicket.html", context)

def getTicketPrice(request, event_id):
    event = Event.objects.get(pk=event_id)
    quantity = event.ticketPrice
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(quantity, safe=False)

def getBalance(request):
    account = Account.objects.get(user=request.user)
    balance = account.balance
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(balance, safe=False)