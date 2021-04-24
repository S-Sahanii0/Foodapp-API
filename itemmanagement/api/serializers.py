from rest_framework import serializers
from itemmanagement.models import ItemList, Category

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = ('id', 'name', 'description', 'image', 'category')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'c_name', 'c_description', 'c_image')