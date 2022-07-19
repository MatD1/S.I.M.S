import uuid
from django.db import models

# Create your models here.
from inventory.models import GroceryInventory, DairyInventory, BakeryInventory, FreshInventory


class AllInventory(models.Model):
    All_Inventory_Last_Reset = models.DateField(auto_now=True)
    Grocery = models.ManyToManyField(GroceryInventory, default="N/A", blank=True)
    Dairy = models.ManyToManyField(DairyInventory, default="N/A", blank=True)
    Bakery = models.ManyToManyField(BakeryInventory, default="N/A", blank=True)
    Fresh = models.ManyToManyField(FreshInventory, default="N/A", blank=True)

    class Meta:
        verbose_name_plural = "All Inventory"

    def __unicode__(self):
        return self.All_Inventory_Last_Reset
