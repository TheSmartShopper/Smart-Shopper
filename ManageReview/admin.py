from django.contrib import admin

# Register your models here.
from ManageReview.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_filter = ['rating']
    list_display = ['text', "rating"]
    list_editable = ['text', "rating"]
    search_fields = ['text']
    list_display_links = None


admin.site.register(Review, ReviewAdmin)
