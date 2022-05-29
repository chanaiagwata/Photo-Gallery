from django.http  import Http404
from .models import Image, Location, Category
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    
    gallery = Image.objects.all()
    return render(request, 'index.html', {'gallery':gallery})

def about(request):
    return render(request, 'about.html')

def gallery(request):
    
    gallery = Image.objects.all()
    return render(request, 'gallery.html', {'gallery':gallery})

def art(request):
    
    art_category = Category.objects.get(id = 1)
    art = Image.objects.filter(category=art_category)
    return render(request, 'category/art.html', {'art':art})

def food(request):
    food_category = Category.objects.get(id = 3)
    food = Image.objects.filter(category=food_category)
    return render(request, 'category/food.html', {'food':food})

def nature(request):
    nature_category = Category.objects.get(id= 3)
    nature = Image.objects.filter(category=nature_category)
    return render(request, 'category/nature.html', {'nature':nature})

def sports(request):
    sports_category = Category.objects.get(id = 2)
    sports = Image.objects.all().filter(category=sports_category)
    return render(request, 'category/sports.html', {'sports':sports})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})