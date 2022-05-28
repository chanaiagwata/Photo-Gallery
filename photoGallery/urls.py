from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index,name = 'indexpage'),
    url('about', views.about, name='aboutpage'),
    url('gallery', views.gallery, name='gallerypage'),
    url('category/art', views.art, name = 'artpage'),
    url('category/food', views.food, name = 'foodpage'),
    url('category/nature', views.nature, name = 'naturepage'),
    url('category/sports', views.sports, name = 'sportspage')
]
