from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions


from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class FoodListView(viewsets.ReadOnlyModelViewSet):
    queryset = FoodCategory.objects.filter(food__isnull=False).distinct()
    serializer_class = FoodListSerializer
