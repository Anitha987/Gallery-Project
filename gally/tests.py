from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.giraffe=Image()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.giraffe,Image)) 
class LocationTestClass(TestCase):
    def setUp(self):
        self.rwanda=Location()

    def test_instance(self):
        self.assertTrue(isinstance(self.rwanda,Location))    
  
class CategoryTestLocation(TestCase):
    def setUp(self):
        self.animal=Category()
    def test_instance(self):    
        self.assertTrue(isinstance(self.animal,Category))            
    
    




