from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import BakeryInventory, DairyInventory, FreshInventory, GroceryInventory
from .serializers import BakeryInvetorySerializer, DairyInvetorySerializer, FreshInvetorySerializer, GroceryInvetorySerializer

# Create your views here.
class GroceryInvetoryViewSet(viewsets.ModelViewSet):
    queryset = GroceryInventory.objects.all().order_by('id')
    serializer_class = GroceryInvetorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_UUID']
    order_fields = ['id']

class DairyInvetoryViewSet(viewsets.ModelViewSet):
    queryset = DairyInventory.objects.all().order_by('id')
    serializer_class = DairyInvetorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_UUID']
    order_fields = ['id']

class BakeryInvetoryViewSet(viewsets.ModelViewSet):
    queryset = BakeryInventory.objects.all().order_by('id')
    serializer_class = BakeryInvetorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_UUID']
    order_fields = ['id']

class FreshInvetoryViewSet(viewsets.ModelViewSet):
    queryset = FreshInventory.objects.all().order_by('id')
    serializer_class = FreshInvetorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_UUID']
    order_fields = ['id']


































