from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from foods.views import FoodListView


api_v1_router = routers.DefaultRouter()
api_v1_router.register('foods', FoodListView)


urlpatterns = [
    path('api/v1/', include(api_v1_router.urls))
]
