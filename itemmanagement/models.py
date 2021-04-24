from django.db import models

class Category(models.Model):
    c_name = models.CharField(max_length = 50, blank = False)
    c_description = models.TextField(null = True)
    c_image =  models.FileField(upload_to = "images/", null = True)

    def __str__(self):
        return self.c_name
        
class ItemList(models.Model):
    name = models.CharField(max_length = 50, blank = False)
    description = models.TextField(null = True)
    image =  models.FileField(upload_to = "images/", null = True)
    category = models.ForeignKey(Category, null = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
# Create your models here.

