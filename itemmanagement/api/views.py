from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from itemmanagement.api.serializers import ItemListSerializer, CategorySerializer
from itemmanagement.models import ItemList, Category

class ApiListItem(ListAPIView):
    queryset = ItemList.objects.all()
    serializer_class = ItemListSerializer
    