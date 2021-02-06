from django.contrib import admin

from ManageStore.models import Store, Section, AD_imags


class StoreAdmin(admin.ModelAdmin):
    fields = ['products', 'StoreOffers']
    list_filter = ["name", 'sections', 'type', 'state', 'join_at', 'products', 'StoreReviews', 'new', 'StoreOffers']
    list_display = ['name', 'start_hours', 'close_hours', 'type', "phonesNumber", 'state', 'join_at', 'new', 'url',
                    'image']
    list_editable = ['type', 'state', 'new', 'image']
    search_fields = ['name']
    list_display_links = ['name']


class SectionAdmin(admin.ModelAdmin):
    list_filter = ["name"]
    list_display = ['name']
    list_editable = ['name']
    search_fields = ['name']
    list_display_links = None


admin.site.register(Store, StoreAdmin)
admin.site.register(AD_imags)
admin.site.register(Section, SectionAdmin)
