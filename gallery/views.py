from django.shortcuts import render
from django.http  import HttpResponse
from .models import Images, Location, Category

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')


def img(request):
    category = Category.get_category()
    images = Images.get_all_images()
    images_location = Location.get_location()
    return render(request,'images.html', {'category': category, 'images': images, 'images_location': images_location})