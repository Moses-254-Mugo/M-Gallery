from django.shortcuts import render
from django.http  import HttpResponse
from .models import Images, Location, Category

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def Home(request):
    category = Category.get_category()
    images = Images.get_all_images()
    images_location = Location.get_location()
    return render(request,'Home.html', {'category': category, 'images': images, 'images_location': images_location})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Images.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})