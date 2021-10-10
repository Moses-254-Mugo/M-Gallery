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

class LocationTestClass(TestCase):
    def setUp(self):
        self.Moringa = Location(location='London')

    def test_instance(self):
        self.assertTrue(isinstance(self.Moringa,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.Moringa.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.Moringa.delete_location('London')
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.Food = Category(category='Football')

    def test_instance(self):
        self.assertTrue(isinstance(self.Food,Category))

    def tearDown(self):
        Category.objects.all().delete()

    def test_save_method(self):
        self.Food.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        self.Food.delete_category('Football')
        category = Category.objects.all()
        self.assertTrue(len(category)==0)