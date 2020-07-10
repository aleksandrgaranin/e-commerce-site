from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.site_header = "Decor Online"
admin.site.site_title = "Decor Online"
admin.site.index_title = "Manage Decor Online"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = "Default Category"
    list_display = ('title','price','discount_price', 'category', 'description',)
    search_fields = ('title','description','category',)
    actions = ('change_category_to_default',)


admin.site.register(Products, ProductAdmin)
admin.site.register(Order)