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
from django_filters.rest_framework import DjangoFilterBackend

class ApiListItem(ListAPIView):
    queryset = ItemList.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name']

class ApiListCategory(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

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

class list_order(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['customer']

class ApiListByCategory(ListAPIView):
    # queryset = ItemList.objects.all()
    serializer_class = ItemListSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = ItemList.objects.all()
        print(self.request.query_params)
        c_name = self.request.query_params.get('c_name')
        category = Category.objects.filter(c_name = c_name)[0]
        queryset = queryset.filter(category=category)
        print(queryset)
        return queryset

@api_view(['POST', ])
def bomb_order(request, id):
    
    order = Order.objects.get(id = id)
    data = {}
    if request.method == 'POST':
        order.status = True
        order.save()
        data['response'] = 'Order completed'
    return Response(data)