# SIMS - Store Inventory Management System

from . import views
from django.urls import include, path
from rest_framework import routers

# Exposes views as a REST URL
SIMSRouter = routers.DefaultRouter()

# Grocery otherwise known as regular packaged food
SIMSRouter.register(r'grocery-inventory', views.GroceryInventoryViewSet),
# Dairy Products, otherwise known as milk, cheese, yogurt, dips etc
SIMSRouter.register(r'dairy-inventory', views.DairyInventoryViewSet),
# Bakery Products, otherwise known as bread products
SIMSRouter.register(r'bakery-inventory', views.BakeryInventoryViewSet),
# Fresh Products, otherwise known as fresh fruit, vegetables, etc
SIMSRouter.register(r'fresh-inventory', views.FreshInventoryViewSet),

urlpatterns = [
    path('V1/inventory/', include(SIMSRouter.urls)),
]
