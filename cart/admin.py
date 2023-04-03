from django.contrib import admin

from cart import models

admin.site.register(models.CartItem)
admin.site.register(models.FinalOrder)