import uuid

from django.contrib import admin
from django.db import models


# Create your models here.

class GroceryInventory(models.Model):
    Item_Inventory_UUID = models.UUIDField(unique=True, default=uuid.uuid4, verbose_name='Unique Inventory UUID',
                                           editable=False)
    Item_Name = models.CharField(max_length=100, unique=True, verbose_name="Item Name")
    Item_Image = models.ImageField(upload_to='assets/', default='assets/S.I.M.S.png')
    Item_SOH = models.IntegerField(default=0, verbose_name="Item Stock On Hand")
    Item_Price = models.FloatField(default=0.00, verbose_name="Item Price")
    Item_Is_On_Sale = models.BooleanField(default=False, verbose_name="Is This Item On Sale?")
    Item_Is_New = models.BooleanField(default=False, verbose_name="Is This Item a New Product / Line")
    Item_Weight_Grams = models.IntegerField(default=0, verbose_name="Item Weight In Grams")
    Item_Last_Received = models.DateField(verbose_name="Item was Last Received On", default=None)
    Item_Next_Delivery = models.DateField(verbose_name="Item Will Be Received On", default=None)
    Item_First_Added = models.DateField(auto_now=True, editable=False)

    class Meta:
        verbose_name_plural = "Grocery Inventory"

    def __str__(self):
        return self.Item_Name


class GroceryInventoryAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Item_Inventory_UUID', 'Item_Name', 'Item_Price', 'Item_Is_On_Sale', 'Item_Is_New']


class DairyInventory(models.Model):
    Item_Inventory_UUID = models.UUIDField(unique=True, default=uuid.uuid4, verbose_name='Unique Inventory UUID',
                                           editable=False)
    Item_Name = models.CharField(max_length=100, unique=True, verbose_name="Item Name")
    Item_Image = models.ImageField(upload_to='assets/', default='assets/S.I.M.S.png')
    Item_SOH = models.IntegerField(default=0, verbose_name="Item Stock On Hand")
    Item_Price = models.FloatField(default=0.00, verbose_name="Item Price")
    Item_Is_On_Sale = models.BooleanField(default=False, verbose_name="Is This Item On Sale?")
    Item_Is_New = models.BooleanField(default=False, verbose_name="Is This Item a New Product / Line")
    Item_Weight_Grams = models.IntegerField(default=0, verbose_name="Item Weight In Grams")
    Item_Last_Received = models.DateField(verbose_name="Item was Last Received On", default=None)
    Item_Next_Delivery = models.DateField(verbose_name="Item Will Be Received On", default=None)
    Item_First_Added = models.DateField(auto_now=True, editable=False)

    class Meta:
        verbose_name_plural = "Dairy Inventory"

    def __str__(self):
        return self.Item_Name


class DairyInventoryAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Item_Inventory_UUID', 'Item_Name', 'Item_Price', 'Item_Is_On_Sale', 'Item_Is_New']


class BakeryInventory(models.Model):
    Item_Inventory_UUID = models.UUIDField(unique=True, default=uuid.uuid4, verbose_name='Unique Inventory UUID',
                                           editable=False)
    Item_Name = models.CharField(max_length=100, unique=True, verbose_name="Item Name")
    Item_Image = models.ImageField(upload_to='assets/', default='assets/S.I.M.S.png')
    Item_SOH = models.IntegerField(default=0, verbose_name="Item Stock On Hand")
    Item_Price = models.FloatField(default=0.00, verbose_name="Item Price")
    Item_Is_On_Sale = models.BooleanField(default=False, verbose_name="Is This Item On Sale?")
    Item_Is_New = models.BooleanField(default=False, verbose_name="Is This Item a New Product / Line")
    Item_Weight_Grams = models.IntegerField(default=0, verbose_name="Item Weight In Grams")
    Item_Last_Received = models.DateField(verbose_name="Item was Last Received On", default=None)
    Item_Next_Delivery = models.DateField(verbose_name="Item Will Be Received On", default=None)
    Item_First_Added = models.DateField(auto_now=True, editable=False)

    class Meta:
        verbose_name_plural = "Bakery Inventory"

    def __str__(self):
        return self.Item_Name


class BakeryInventoryAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Item_Inventory_UUID', 'Item_Name', 'Item_Price', 'Item_Is_On_Sale', 'Item_Is_New']


class FreshInventory(models.Model):
    Item_Inventory_UUID = models.UUIDField(unique=True, default=uuid.uuid4, verbose_name='Unique Inventory UUID',
                                           editable=False)
    Item_Name = models.CharField(max_length=100, unique=True, verbose_name="Item Name")
    Item_Image = models.ImageField(upload_to='assets/', default='assets/S.I.M.S.png')
    Item_SOH = models.IntegerField(default=0, verbose_name="Item Stock On Hand")
    Item_Price = models.FloatField(default=0.00, verbose_name="Item Price")
    Item_Is_On_Sale = models.BooleanField(default=False, verbose_name="Is This Item On Sale?")
    Item_Is_New = models.BooleanField(default=False, verbose_name="Is This Item a New Product / Line")
    Item_Weight_Grams = models.IntegerField(default=0, verbose_name="Item Weight In Grams")
    Item_Last_Received = models.DateField(verbose_name="Item was Last Received On", default=None)
    Item_Next_Delivery = models.DateField(verbose_name="Item Will Be Received On", default=None)
    Item_First_Added = models.DateField(auto_now=True, editable=False)

    class Meta:
        verbose_name_plural = "Fresh Inventory"

    def __str__(self):
        return self.Item_Name


class FreshInventoryAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Item_Inventory_UUID', 'Item_Name', 'Item_Price', 'Item_Is_On_Sale', 'Item_Is_New']
