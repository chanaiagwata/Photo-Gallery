from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'indexpage'),
    url(r'about', views.about, name='aboutpage'),
    url(r'gallery', views.gallery, name='gallerypage'),
    url(r'category/art', views.art, name = 'artpage'),
    url(r'category/food', views.food, name = 'foodpage'),
    url(r'category/nature', views.nature, name = 'naturepage'),
    url(r'category/sports', views.sports, name = 'sportspage')
]
