from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length =30)
    description= models.CharField(max_length =60)
    location=models.ForeignKey(Location)

    def __str__(self):
        return self.first_name

class Location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location
