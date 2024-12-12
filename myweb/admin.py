from django.contrib import admin
from .models import  Package,Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_name', 'phone')


class PackageAdmin(admin.ModelAdmin):
    list_display = ( 'description', 'price','approved')
    list_filter = ('approved',)



admin.site.register(Vendor, VendorAdmin)
admin.site.register(Package, PackageAdmin)



