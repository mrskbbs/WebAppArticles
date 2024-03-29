from django.urls import path
from .views import *

app_name = 'articles'
urlpatterns = [
    path('<int:id>', article, name = 'article'),
    path('<int:id>/create', create, name = 'create'),
    path('<int:id>/delete', delete, name = 'delete'),
    path('<int:id>/edit', edit, name = 'edit'),
]