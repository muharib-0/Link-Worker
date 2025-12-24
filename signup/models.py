from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class userprofile(AbstractUser):
    ROLES = (
        ('client', 'Client'),
        ('worker', 'Worker'),
    )
   
    
    role=models.CharField(max_length=50, choices=ROLES)

    def __str__(self):
        return self.username