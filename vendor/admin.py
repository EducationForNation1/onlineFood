from django.contrib import admin
from .models import Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display =  ['user','verdor_name', 'is_approved', 'created_at']
    list_display_links = ['user','verdor_name']

# Register your models here.

admin.site.register(Vendor,VendorAdmin)