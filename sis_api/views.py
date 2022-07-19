from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from inventory.models import BakeryInventory, DairyInventory, FreshInventory, GroceryInventory
from .serializers import BakeryInventorySerializer, DairyInventorySerializer, FreshInventorySerializer, \
    GroceryInventorySerializer


# Create your views here.
class GroceryInventoryViewSet(viewsets.ModelViewSet):
    queryset = GroceryInventory.objects.all().order_by('id')
    serializer_class = GroceryInventorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    order_fields = ['id']


class DairyInventoryViewSet(viewsets.ModelViewSet):
    queryset = DairyInventory.objects.all().order_by('id')
    serializer_class = DairyInventorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    order_fields = ['id']


class BakeryInventoryViewSet(viewsets.ModelViewSet):
    queryset = BakeryInventory.objects.all().order_by('id')
    serializer_class = BakeryInventorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    order_fields = ['id']


class FreshInventoryViewSet(viewsets.ModelViewSet):
    queryset = FreshInventory.objects.all().order_by('id')
    serializer_class = FreshInventorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    order_fields = ['id']
