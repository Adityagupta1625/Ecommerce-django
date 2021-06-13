from django.contrib import admin
from .models import Order, OrderUpdate, Product,Contact

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)

# Register your models here.
