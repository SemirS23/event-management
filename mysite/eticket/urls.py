from django.urls import path, re_path


from . import views
app_name = 'eticket'
urlpatterns = [
    path("", views.home, name="home"),
    path("venue/", views.venue, name="venue"),
]   