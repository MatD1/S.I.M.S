from django.contrib import admin

from .models import BakeryInventory, DairyInventory, FreshInventory, GroceryInventory

# Register your models here.
admin.site.register(GroceryInventory)
admin.site.register(DairyInventory)
admin.site.register(BakeryInventory)
admin.site.register(FreshInventory)
