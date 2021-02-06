from ManageProduct.models import Product
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_filter = ["price", 'manufacturer', 'ProductReview', 'product_sections', 'par_Code', ]
    list_display = ['name', "price", "number_Of_Copy", 'manufacturer', 'product_sections', 'discount', 'slug', 'image']
    # list_editable=['']
    search_fields = ['name', 'description']
    list_display_links = ['name']


admin.site.register(Product, ProductAdmin)
