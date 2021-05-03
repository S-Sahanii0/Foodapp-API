from django.contrib import admin
from itemmanagement.models import ItemList, Category , Order

# Register your models here.
admin.site.register(ItemList)
admin.site.register(Category)
admin.site.register(Order)