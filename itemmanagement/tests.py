import json 

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from itemmanagement.api.serializers import ItemListSerializer, CategorySerializer
from itemmanagement.models import ItemList, Category, Order
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from account.models import Account


class ListItemTestCase(APITestCase):

    def testItem(self):
        category_list = Category.objects.create(c_name = "Fastfood")
        ItemList.objects.create(name="pizza", category = category_list)
        response = self.client.get("/api/items")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class OrderTestCase(APITestCase):
    client = 1
    def testOrder(self):
        Account.objects.create_user(email = "test@gmail.com", firstname ="test1", lastname ="test1", 
                phone=982827287, password="strongpass")
        user = Account.objects.get(email = "test@gmail.com")
        token = Token.objects.get(user= user.id)
        print(token)
        client = APIClient()
        client.force_authenticate(user=user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        category_list = Category.objects.create(c_name = "Fastfood")
        item_list = ItemList.objects.create(id =5, name="pizza", category = category_list)
        data = {
            "customer" : user,
            "quantity": 1
        }
        # Order.objects.create(item = item_list, category = category_list)
        response = client.post("/api/order/5", data, )
        
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    