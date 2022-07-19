import uuid
from django.db import models


# Create your models here.

class GroceryInventory(models.Model):
    Item_Inventory_UUID = models.UUIDField(unique=True, default=uuid.uuid4, verbose_name='Unique Inventory UUID')
    Item_Name = models.CharField(max_length=100, unique=True, verbose_name="Item Name")
    Item_Amount = models.IntegerField(default=0, verbose_name="Item Amount")
    Item_Last_Received = models.DateField(verbose_name="Item was Last Received On", default=None)
    Item_Next_Delivery = models.DateField(verbose_name="Item Will Be Received On", default=None)
    Item_First_Added = models.DateField(auto_now=True, editable=False)

    class Meta:
        verbose_name_plural = "Grocery Inventory"

    def __str__(self):
        return self.Item_Name


class DairyInventory(models.Model):
    Item_Inventory_UUID = models.UUIDField(unique=True, default=uuid.uuid4, verbose_name='Unique Inventory UUID')
    Item_Name = models.CharField(max_length=100, unique=True, verbose_name="Item Name")
    Item_Amount = models.IntegerField(default=0, verbose_name="Item Amount")
    Item_Last_Received = models.DateField(verbose_name="Item was Last Received On", default=None)
    Item_Next_Delivery = models.DateField(verbose_name="Item Will Be Received On", default=None)
    Item_First_Added = models.DateField(auto_now=True, editable=False)

    class Meta:
        verbose_name_plural = "Dairy Inventory"

    def __str__(self):
        return self.Item_Name


class BakeryInventory(models.Model):
    Item_Inventory_UUID = models.UUIDField(unique=True, default=uuid.uuid4, verbose_name='Unique Inventory UUID')
    Item_Name = models.CharField(max_length=100, unique=True, verbose_name="Item Name")
    Item_Amount = models.IntegerField(default=0, verbose_name="Item Amount")
    Item_Last_Received = models.DateField(verbose_name="Item was Last Received On", default=None)
    Item_Next_Delivery = models.DateField(verbose_name="Item Will Be Received On", default=None)
    Item_First_Added = models.DateField(auto_now=True, editable=False)

    class Meta:
        verbose_name_plural = "Bakery Inventory"

    def __str__(self):
        return self.Item_Name


class FreshInventory(models.Model):
    Item_Inventory_UUID = models.UUIDField(unique=True, default=uuid.uuid4, verbose_name='Unique Inventory UUID')
    Item_Name = models.CharField(max_length=100, unique=True, verbose_name="Item Name")
    Item_Amount = models.IntegerField(default=0, verbose_name="Item Amount")
    Item_Last_Received = models.DateField(verbose_name="Item was Last Received On", default=None)
    Item_Next_Delivery = models.DateField(verbose_name="Item Will Be Received On", default=None)
    Item_First_Added = models.DateField(auto_now=True, editable=False)

    class Meta:
        verbose_name_plural = "Fresh Inventory"

    def __str__(self):
        return self.Item_Name
