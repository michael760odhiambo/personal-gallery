from django.test import TestCase
from photo.models import Image,Location,Category
import datetime

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
