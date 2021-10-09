from django.http.response import Http404
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Images, Location, Category
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def Home(request):
    category = Category.get_category()
    # images = Images.get_all_images()
    images_location = Location.get_location()
    return render(request,'Home.html', {'category': category, 'images_location': images_location})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Images.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def single_image(request, id):
    try:
        photo = Images.objects.get(id = id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, "single_image.html",{"photo":photo})
    
def search_by_location(request, location):
    location_image = Images.filter_by_location(location)
    return render(request,'location.html', {"location_image":location_image})
    
