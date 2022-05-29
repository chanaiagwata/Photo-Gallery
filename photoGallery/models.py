from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60, unique='True')
    
    class meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length =80)
    category = models.ForeignKey(Category)
    description = models.TextField()
    location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    