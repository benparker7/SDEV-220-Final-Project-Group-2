from django.db import models

# Create your models here.

class Users(models.Model):
    user_text = models.CharField(max_length=24)
    user_pass = models.CharField(max_length=64)

    def __str__(self):
        return self.user_text, self.user_pass