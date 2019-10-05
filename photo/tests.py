from django.test import TestCase
from photo.models import Image,Location,Category
import datetime

class TestLocation(TestCase):
    def setUp(self):
        self.place = Location(place='ngong',address='1234', city='Nairobi')
    def test_instance(self):
        self.assertTrue(isinstance(self.place, Location)  

    def test_save_method(self):
        self.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)  

class   CategoryTest(TestCase):
    def setUp(TestCase):
        self.title = Category(created_at='', updated_at='', title='', group='')
    def test_instance(self):
        self.assertTrue(isinstance(self.title, Category)
        )
    def test_save_method(self):
        self.title.save_categories()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0 )                   

class ImageTest(TestCase):
    def setUp(self):
        self.name = Image(name='sunshine', description='A sunshine image', post_date='date')
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Image))

    def test_save_method(self):
        self.name.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
            
# Create your tests here.
