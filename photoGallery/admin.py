from django.contrib import admin
from .models import Category, Location, Image

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
        
class ImageAdmin(admin.ModelAdmin):
    list_display = ['name','category','location','pub_date']
    ordering = ['-pub_date']
    
    

    
    

    


# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)