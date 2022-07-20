from rest_framework import serializers

from inventory.models import BakeryInventory, DairyInventory, FreshInventory, GroceryInventory
from .models import AllInventory


class GroceryInventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroceryInventory
        fields = ['id', 'Item_Name', 'Item_SOH', 'Item_Price', 'Item_Is_On_Sale', 'Item_Is_New', 'Item_Weight_Grams',
                  'Item_Inventory_UUID', 'Item_Last_Received', 'Item_Next_Delivery',
                  'Item_First_Added']


class DairyInventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DairyInventory
        fields = ['id', 'Item_Name', 'Item_SOH', 'Item_Price', 'Item_Is_On_Sale', 'Item_Is_New', 'Item_Weight_Grams',
                  'Item_Inventory_UUID', 'Item_Last_Received', 'Item_Next_Delivery',
                  'Item_First_Added']


class BakeryInventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BakeryInventory
        fields = ['id', 'Item_Name', 'Item_SOH', 'Item_Price', 'Item_Is_On_Sale', 'Item_Is_New', 'Item_Weight_Grams',
                  'Item_Inventory_UUID', 'Item_Last_Received', 'Item_Next_Delivery',
                  'Item_First_Added']


class FreshInventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FreshInventory
        fields = ['id', 'Item_Name', 'Item_SOH', 'Item_Price', 'Item_Is_On_Sale', 'Item_Is_New', 'Item_Weight_Grams',
                  'Item_Inventory_UUID', 'Item_Last_Received', 'Item_Next_Delivery',
                  'Item_First_Added']

class AllInventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllInventory
        fields = ['id', 'All_Inventory_Last_Reset', 'Grocery', 'Dairy', 'Bakery', 'Fresh']
