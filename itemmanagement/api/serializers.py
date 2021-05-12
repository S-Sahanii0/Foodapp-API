from rest_framework import serializers
from itemmanagement.models import ItemList, Category, Order


        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'c_name', 'c_description', 'c_image_url')

class ItemListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('get_category')
    class Meta:

        model = ItemList
        fields = ('id', 'name', 'description', 'image_url', 'category')

    def get_category(self, ItemList):
        category = ItemList.category.c_name
        return category

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField('get_customer')
    item = serializers.SerializerMethodField('get_item')

    class Meta:
        model = Order
        fields = ('customer', 'item', 'quantity', 'time')
        

    def get_customer(self, Order):
        customer = Order.customer.email
        return customer

    def get_item(self, Order):
        item = Order.item.name
        return item
    


   

    

