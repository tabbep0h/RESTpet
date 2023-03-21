from django.contrib import admin
from .models import *

admin.site.register(Pet)
admin.site.register(Order)
admin.site.register(PetStatus)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(OrderStatus)
