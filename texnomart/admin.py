from django.contrib import admin
from texnomart import models
# Register your models here.

admin.site.register(models.Image)
admin.site.register(models.Attribute)
admin.site.register(models.AttributeValue)
admin.site.register(models.ProductAttribute)
admin.site.register(models.Comment)

@admin.register(models.Category)
class CategoryModelAdmin(admin.ModelAdmin):
    
    list_display = ['category_name','slug']
    prepopulated_fields = {'slug':('category_name',)}

@admin.register(models.Product)
class ProductModelAdmin(admin.ModelAdmin):
    
    list_display = ['product_name','slug']
    prepopulated_fields = {'slug':('product_name',)}