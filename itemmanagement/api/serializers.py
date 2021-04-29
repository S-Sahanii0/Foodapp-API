from rest_framework import serializers
from itemmanagement.models import ItemList, Category, Order

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = ('id', 'name', 'description', 'image', 'category')
        depth = 1

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'c_name', 'c_description', 'c_image')

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField('get_customer')
    

    class Meta:
        model = Order
        fields = ('customer', 'item', 'quantity', 'time')
        depth = 1 

    def get_customer(self, Order):
        customer = Order.customer.email
        return customer

   

    

