from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Images(models.Model):
    
    # image = models.ImageField(upload_to='images/')
    image = CloudinaryField('image')
    name = models.CharField(max_length=60)
    description= models.CharField(max_length=200)
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
    def get_single_image(cls,id):
        img = cls.objects.filter(id=id)

        return img

    @classmethod
    def search_by_name(cls,search_term):
        image = cls.objects.filter(name__icontains=search_term)
        return image

    @classmethod
    def view_image_by_location(cls,location):
        location_image = cls.objects.filter(location = location)
        return location_image   

    @classmethod
    def view_image_by_category(cls,category):
        category = cls.objects.filter(category = category)
        return category
        
   






class Location(models.Model):
    location_name = models.CharField(max_length=50)

    def save_location(self):
        self.save()


    def __str__(self):
        return self.location_name
    
    def delete_location(self):
        self.delete()

    @classmethod
    def get_location(cls):
        location = cls.objects.all()
        return location

    
    



class Category(models.Model):
    category_name = models.CharField(max_length=80)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


    @classmethod
    def get_category(cls):
        categories= cls.objects.all()
        return categories


    def __str__(self):
        return self.category_name
    