from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =30)
    description= models.CharField(max_length =30)
    # email = models.EmailField()

    def __str__(self):
        return self.first_name

class location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location
