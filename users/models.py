from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30, default = None)
    password = models.CharField(max_length = 64, default = None)

    def __str__(self):
        return f"User: {self.username}\nID: {self.pk}\nPassword hash: {self.password}\n\n"