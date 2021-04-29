from django.db import models
from account.models import Account
from datetime import datetime

class Category(models.Model):
    c_name = models.CharField(max_length = 50, blank = False)
    c_description = models.TextField(null = True)
    # c_image =  models.ImageField(upload_to = "images/")
    c_image_url = models.URLField(null =  True)

    def __str__(self):
        return self.c_name
    
    # def get_remote_image(self):
    #     if self.c_image_url and not self.c_image:
    #         result = urllib.urlretrieve(Self.c_image_url)
    #         self.c_image.save(
    #             os.path.basename(self.c_image_url),
    #             File(open(result[0]))
    #         )
    #         self.save()
        
class ItemList(models.Model):
    name = models.CharField(max_length = 50, blank = False)
    description = models.TextField(null = True)
    # image =  models.FileField(upload_to = "images/", null = True)
    c_image_url = models.URLField(null = True)
    category = models.ForeignKey(Category, null = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Account, null = True, on_delete = models.CASCADE)
    item = models.ForeignKey(ItemList, null = True, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1)
    time = models.DateTimeField(default = datetime.now, null = True)

    def __str__(self):
        return self.item.name


