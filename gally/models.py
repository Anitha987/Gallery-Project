from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.ImageField()
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =60)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name

class Location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField() 

    def __str__(self):
        return self.category     



