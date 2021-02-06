from django.contrib import admin

from .CustomerProfilemodel import CustomerProfile
from .models import StoreAdminProfile  # ,Favorite


class CustomerProfileAdmin(admin.ModelAdmin):
    list_filter = ["user", 'country', 'address', 'join_at']
    list_display = ['user', "country", 'address', 'join_at', 'image', 'slug']
    list_editable = ['address']
    # search_fields=['use']#__for relation
    list_display_links = ['user']


class StoreAdminProfileAdmin(admin.ModelAdmin):
    list_filter = ["user", 'store', 'country', 'address', 'join_at']
    list_display = ['user', 'store', "country", 'address', 'join_at', 'image', 'slug']
    list_editable = ['store', "country", 'address', 'join_at', 'image', 'slug']
    search_fields = ['store__name']
    list_display_links = ['user']


admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(StoreAdminProfile, StoreAdminProfileAdmin)
