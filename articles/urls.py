from django.urls import path
from .views import *

app_name = 'articles'
urlpatterns = [
    path('<int:id>', articleView, name = 'article'),
    path('create', createView, name = 'create'),
    path('<int:id>/delete', deleteView, name = 'delete'),
    path('<int:id>/edit', editView, name = 'edit'),
]