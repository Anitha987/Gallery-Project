from django.db import models


# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length =30) 

    def __str__(self):
        return self.category     

class Image(models.Model):
    image =  models.ImageField(upload_to = 'pictures/',null=True)
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =60)
    location = models.ForeignKey(Location ,null=True)
    category = models.ForeignKey(Category,null=True)
 

    def save_image(self):
        self.save()
    def __str__(self):
        return self.name
    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__category__icontains=search_term)
        return image   

    def filter_by_location(cls,location):
        image = cls.objects.filter(location_location_icontains=location) 
        return image   

