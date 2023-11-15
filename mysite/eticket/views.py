from django.shortcuts import redirect, render
from .models import Venue

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