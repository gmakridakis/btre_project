from django.contrib import admin
from contacts.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "contact_date", "listing")
    search_fields = ("name", "email", "listing")

    list_per_page = 37


admin.site.register(Contact, ContactAdmin)