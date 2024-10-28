from django.db import models

# Create your models here.
class Services(models.Model):
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    city = models.CharField(max_length=15)
    zipp = models.CharField(max_length=10)

    def __str__(self) :
        return self.email
