from django.db import models
from users.models import User
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 64, default = None)
    author = models.ForeignKey(User, on_delete = models.CASCADE, default = None)
    published = models.BooleanField(default = False)
    date = models.DateTimeField(default = None)
    content = models.JSONField(default = dict)
    likes = models.IntegerField(default = 0)

    def __str__(self):
        return f"Article: {self.title}\nID: {self.pk}\nDate: {self.date}\nLikes: {self.likes}\n\n"
    # from articles.models import Article
    # a = Article(title = "Hello title", content = "<h1>Big thingy</h1>", likes = 228)