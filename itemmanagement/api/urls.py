from django.urls import path
from itemmanagement.api.views import(
    ApiListItem,
)
app_name = 'itemmanagement'

urlpatterns = [
    path('items', ApiListItem.as_view(), name = 'items'),
]