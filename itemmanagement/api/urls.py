from django.urls import path
from itemmanagement.api.views import(
    ApiListItem,
    order_item,
    list_order,
    ApiListCategory,
    # list_item_by_category,
    ApiListByCategory,
)
app_name = 'itemmanagement'

urlpatterns = [
    path('items', ApiListItem.as_view(), name = 'items'),
    path('categories', ApiListCategory.as_view(), name = 'categories'),
    path('order/<int:id>', order_item, name = 'order'),
    path('list_order', list_order.as_view(), name = 'list_order'),
    path('list_by_category', ApiListByCategory.as_view(), name = 'list_by_category'),
    
]