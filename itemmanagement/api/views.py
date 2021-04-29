from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from itemmanagement.api.serializers import ItemListSerializer, CategorySerializer, OrderSerializer
from itemmanagement.models import ItemList, Category


class ApiListItem(ListAPIView):
    queryset = ItemList.objects.all()
    serializer_class = ItemListSerializer

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def order_item(request, id):
    try:
        item = ItemList.objects.get(id = id)
    
    except ItemList.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    user = request.user
   

    if request.method == "POST":
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(customer = user, item = item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    