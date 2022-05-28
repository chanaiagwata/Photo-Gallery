from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique='True')
    
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


    