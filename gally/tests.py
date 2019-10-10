from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.image=Image(image='pussy.jpg',name='pussy',decription='pretty pussy',location='newyork',category='animals')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))    




