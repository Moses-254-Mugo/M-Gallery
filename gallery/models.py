from django.db import models
from django.db.models.base import Model

# Create your models here.
class Images(models.Model):
    images = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description= models.CharField(max_length=80)
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def save_image(self):
        self.save()

    def __str__(self):
        return self.name

    def delete_image(self):
        self.delete()

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()

        return images


    @classmethod
    def get_image_by_id(cls,id):
        img = cls.objects.filter(id=id)

        return img

    @classmethod
    def search_image_by_category(cls, category):
        image_category = cls.objects.filter(categroy = category)
        return image_category
        
    @classmethod
    def filter_by_location(cls,location):
        image_location = cls.objects.filter(location = location)
        return image_location







class Location(models.Model):
    location_name = models.CharField(max_length=50)

    def save_location(self):
        self.save()

    
    def delete_location(self):
        self.delete()

    @classmethod
    def get_location(cls):
        location = cls.objects.all()
        return location

    def __str__(self):
        return self.location_name
    



class Category(models.Model):
    category_name = models.CharField(max_length=80)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


    @classmethod
    def get_category(cls):
        category = cls.objects.all()
        return category


    def __str__(self):
        return self.category_name
    