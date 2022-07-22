from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django_filters.rest_framework import DjangoFilterBackend

from inventory.models import BakeryInventory, DairyInventory, FreshInventory, GroceryInventory, MeatInventory, \
    DeliInventory
from all_inventory.models import AllInventory
from .serializers import BakeryInventorySerializer, DairyInventorySerializer, FreshInventorySerializer, \
    GroceryInventorySerializer, MeatInventorySerializer, DeliInventorySerializer, AllInventorySerializer


# Create your views here.
class GroceryInventoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = GroceryInventory.objects.all().order_by('id')
    serializer_class = GroceryInventorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    order_fields = ['id']


class DairyInventoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = DairyInventory.objects.all().order_by('id')
    serializer_class = DairyInventorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    order_fields = ['id']


class BakeryInventoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = BakeryInventory.objects.all().order_by('id')
    serializer_class = BakeryInventorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    order_fields = ['id']


class FreshInventoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = FreshInventory.objects.all().order_by('id')
    serializer_class = FreshInventorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    order_fields = ['id']


class MeatInventoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = MeatInventory.objects.all().order_by('id')
    serializer_class = MeatInventorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    order_fields = ['id']


class DeliInventoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = DeliInventory.objects.all().order_by('id')
    serializer_class = DeliInventorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    order_fields = ['id']


class AllInventoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = AllInventory.objects.all().order_by('id')
    serializer_class = AllInventorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    filterset_fields = ['Item_Name', 'id', 'Item_Inventory_UUID']
    order_fields = ['id']
