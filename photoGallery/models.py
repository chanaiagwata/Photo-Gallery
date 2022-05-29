from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60, unique='True')
    
    class meta:
        ordering = ["name"]

        
    def __str__(self):
        return self.name
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=60)
    
    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length =80)
    category = models.ForeignKey(Category)
    description = models.TextField()
    location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to = 'photos/')
    
    
    def __str__(self):
        return self.name
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def get_image_by_id(cls):
        images = cls.objects.get(id =id)
        return images
    @classmethod
    def search_by_name(cls,search_term):
        image = cls.objects.filter(name__icontains=search_term)
        return image