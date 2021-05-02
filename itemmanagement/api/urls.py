from django.urls import path
from itemmanagement.api.views import(
    ApiListItem,
    order_item,
    list_order_item,
    ApiListCategory
)
app_name = 'itemmanagement'

urlpatterns = [
    path('items', ApiListItem.as_view(), name = 'items'),
    path('categories', ApiListCategory.as_view(), name = 'categories'),
    path('order/<int:id>', order_item, name = 'order'),
    path('list_order', list_order_item, name = 'list_order'),
]