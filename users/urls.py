from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path("<int:id>", profile, name = "profile"),
    path("login", login, name = "login"),
    path("signup", signup, name = "signup"),
]