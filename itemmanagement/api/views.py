from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from itemmanagement.api.serializers import ItemListSerializer, CategorySerializer, OrderSerializer
from itemmanagement.models import ItemList, Category, Order
from rest_framework.filters import SearchFilter, OrderingFilter

class ApiListItem(ListAPIView):
    queryset = ItemList.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name']

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def order_item(request):
    user = request.user
    try:
        
        ordered_items = Order.objects.filter(customer = user)[0]
    
    except IndexError as e:
        data = {}
        data['response'] = ['No items ordered yet']
        return Response(data, status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = OrderSerializer(ordered_items)
        return Response(serializer.data)

    



    