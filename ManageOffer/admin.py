from django.contrib import admin

from ManageOffer.models import Offer


class ManageOfferAdmin(admin.ModelAdmin):
    list_filter = ["name", 'products', 'state', 'expiratiDate', 'number_OF_Copy', 'price']
    list_display = ["name", 'state', 'expiratiDate', 'number_OF_Copy', 'price']
    list_editable = ["expiratiDate", ]
    search_fields = ['name']
    list_display_links = ['name']


admin.site.register(Offer, ManageOfferAdmin)
