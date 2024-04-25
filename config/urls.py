from django.urls import path
from restaurant.views import FoodsListView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/foods/', FoodsListView.as_view(), name='foods-list'),
]