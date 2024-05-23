
from django.db import models



# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    work = models.CharField(max_length=255)

    def __str__(self):
        return self.name
