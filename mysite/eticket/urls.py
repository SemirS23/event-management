from django.urls import path, re_path


from . import views
app_name = 'eticket'
urlpatterns = [
    path("", views.home, name="home"),
    path("venue/", views.venue, name="venue"),
    path("event/", views.hostEvent, name="event"),
    path("ticket/", views.buyTickets, name="ticket"),
    path("get_ticket_price/<str:event_id>/", views.getTicketPrice, name="getTicketPrice"),
    path("get_balance/", views.getBalance, name="getBalance"),
]   