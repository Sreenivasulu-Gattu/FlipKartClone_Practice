from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(UserModel)
admin.site.register(Product)
admin.site.register(ProductCat)
admin.site.register(ProductBrand)
