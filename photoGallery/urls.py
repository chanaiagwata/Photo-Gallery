from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index,name = 'indexpage'),
    url('about', views.about, name='aboutpage'),
    url('gallery', views.gallery, name='gallerypage')
]
