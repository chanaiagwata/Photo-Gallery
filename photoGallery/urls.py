from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'indexpage'),
    url(r'about', views.about, name='aboutpage'),
    url(r'gallery', views.gallery, name='gallerypage'),
    url(r'category/art', views.art, name = 'artpage'),
    url(r'category/food', views.food, name = 'foodpage'),
    url(r'category/nature', views.nature, name = 'naturepage'),
    url(r'category/sports', views.sports, name = 'sportspage'),
    url(r'^search/', views.search_results, name='search_results'),
   url(r'^image/(?P<category>\w+)/(?P<id>\d+)', views.image, name='singleImage'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)