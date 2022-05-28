from pydoc import render_doc
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def gallery(request):
    return render(request, 'gallery.html')

def art(request):
    return render(request, 'category/art.html')

def food(request):
    return render(request, 'category/food.html')

def nature(request):
    return render(request, 'category/nature.html')

def sports(request):
    return render(request, 'category/sports.html')