from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path("<int:id>", profileView, name = "profile"),
    path("login", loginView, name = "login"),
    path("logout", logoutView, name = "logout"),
    path("signup", signupView, name = "signup"),
]