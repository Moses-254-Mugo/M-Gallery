from django.test import TestCase
from .models import Images, Location, Category


# Create your tests here.
class ImagesTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.moses = Images(name = 'Moses',location='Nairobi',category= 'love')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.moses,Images))

    # Testing Save method
    def test_save_method(self):
        self.moses.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)