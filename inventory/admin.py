from django.contrib import admin

from .models import BakeryInventory, DairyInventory, FreshInventory, GroceryInventory, GroceryInventoryAdmin, \
    DairyInventoryAdmin, BakeryInventoryAdmin, FreshInventoryAdmin

# Register your models here.
admin.site.register(GroceryInventory, GroceryInventoryAdmin)
admin.site.register(DairyInventory, DairyInventoryAdmin)
admin.site.register(BakeryInventory, BakeryInventoryAdmin)
admin.site.register(FreshInventory, FreshInventoryAdmin)
