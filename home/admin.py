from pyexpat import model
from django.contrib import admin
from .models import (
    Category,
    QuantityVariant,
    ColorVariant,
    SizeVariant,
    Product,
    ProductImage,
)
# Register your models here.


class CategoryAdminModel(admin.ModelAdmin):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'slug', ]


class ProductAdminModel(admin.ModelAdmin):
    class Meta:
        model = Product
        fields = "__all__"


admin.site.register(Category, CategoryAdminModel)
admin.site.register(Product, ProductAdminModel)
admin.site.register(QuantityVariant)
admin.site.register(ColorVariant)
admin.site.register(SizeVariant)
admin.site.register(ProductImage)
