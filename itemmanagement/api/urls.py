from django.urls import path
from itemmanagement.api.views import(
    ApiListItem,
    order_item,
)
app_name = 'itemmanagement'

urlpatterns = [
    path('items', ApiListItem.as_view(), name = 'items'),
    path('order/<int:id>', order_item, name = 'order'),
]