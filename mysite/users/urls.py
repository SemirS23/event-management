from django.urls import path

from . import views
app_name = 'users'
urlpatterns = [
    path("", views.loginPage, name="loginPage"),
    path("register/", views.register, name="register"),
    path("logout/", views.logoutPage, name="logoutPage"),
]