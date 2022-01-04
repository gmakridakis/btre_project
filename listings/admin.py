from django.contrib import admin
from listings.models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "price")
    list_filter = ("title", "is_published")
    #list_editable = ("title","is_published")
    search_fields=("title", "is_published", "state")
    #list_display_links = ()
    list_per_page=5


admin.site.register(Listing, ListingAdmin)