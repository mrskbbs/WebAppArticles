from django.urls import path
from .views import *

app_name = 'articles'
urlpatterns = [
    path('<int:pk>', articleView, name = 'article'),
    path('create', createView, name = 'create'),
    path('<int:pk>/delete', deleteView, name = 'delete'),
    path('<int:pk>/edit', editView, name = 'edit'),
]