import json 

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from account.api.serializers import RegistrationSerializer
from account.models import Account
from django.test import Client

class RegistrationTestCase(APITestCase):

    def testRegistration(self):
        data = {"email": "test@gmail.com", "firstname":"test1", "lastname":"test1", 
                "phone":982827287, "address":"test", "password": "strongpass", "password2":"strongpass"}
        response = self.client.post("/api/account/register", data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testPassword(self):
        data = {"email": "test@gmail.com", "firstname":"test1", "lastname":"test1", 
                "phone":982827287, "address":"test", "password": "strongpass", "password2":"strong"}
        response = self.client.post("/api/account/register", data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
class LoginTestCase(APITestCase):
    def testLogin(self):
        Account.objects.create_user(email = "test@gmail.com", firstname ="test1", lastname ="test1", 
                phone=982827287, password="strongpass")
        data = {"username": "test@gmail.com", 
                 "password": "strongpass"}
        response =self.client.post('/api/account/login', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def testIncorrectPass(self):
        Account.objects.create_user(email = "test@gmail.com", firstname ="test1", lastname ="test1", 
                phone=982827287, password="strongpass")
        data = {"username": "test@gmail.com", 
                 "password": "haha"}
        response =self.client.post('/api/account/login', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    

    
