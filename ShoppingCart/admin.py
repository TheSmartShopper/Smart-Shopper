from django.contrib import admin
from ShoppingCart.models import ShoppingCart, CartItem,CartOffer

class CartItemAdmin(admin.ModelAdmin):
    list_filter = ["product",'added_at','quantity']
    list_display = ["product",'added_at','quantity']
    list_editable = ["product",'quantity']
    search_fields = ['product__name']
    list_display_links = None

class CartOfferAdmin(admin.ModelAdmin):
    list_filter = ['Offer','added_at','quantity']
    list_display = ['Offer','added_at','quantity']
    list_editable = ['Offer','quantity']
    search_fields = ['Offer__name']
    list_display_links = None

class ShoppingCartAdmin(admin.ModelAdmin):
    list_filter = ["items",'offers','is_finished_adding','created_at']
    list_display = ['is_finished_adding','created_at']
    list_editable = ['is_finished_adding','created_at']
    search_fields = ['items__product__name']
    list_display_links = None

admin.site.register(ShoppingCart,ShoppingCartAdmin)
admin.site.register(CartItem,CartItemAdmin)
admin.site.register(CartOffer,CartOfferAdmin)
