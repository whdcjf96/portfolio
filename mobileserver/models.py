from django.db import models

# Create your models here.

class mobileserver(models.Model):
    image = models.ImageField(upload_to='images/')
    text = models.CharField(max_length=300)
