from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 64, default = None)
    author = models.ForeignKey(User, on_delete = models.CASCADE, default = None, related_name = "author")
    published = models.BooleanField(default = False)
    date = models.DateTimeField(default = None)
    content = models.JSONField(default = dict)
    users_liked = models.ManyToManyField(User, related_name = "users_liked")

    def __str__(self) -> str:
        return f"Article: {self.title}\nID: {self.pk}\nDate: {self.date}\nLikes: {self.likes}\n\n"
    
    def countLikes(self) -> int:
        return self.users_liked.count()