from django.db import models
from django.contrib.auth.models import make_password

# Create your models here.
class userprofile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        if not self.pk:  # Hash password only on creation       
            self.password = make_password(self.password)
        return super().save(*args, **kwargs)
    role=models.CharField(max_length=50)

    def __str__(self):
        return self.username