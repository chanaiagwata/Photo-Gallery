from django.test import TestCase

# Create your tests here.
from .models import Location, Category,Image
import datetime as dt

# Create your tests here.

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.loc1= Location(name = 'Lamu')
        
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.loc1,Location))


class CategoryTestClass(TestCase):
    def setUp(self):
        self.cat1 = Category(name = 'Food')




class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.image= Location(name = 'Lamu')
        self.image.save_location()
        
        self.new_image= Image(name = 'China',description = 'Test description',location = self.image)
        self.new_image.save()