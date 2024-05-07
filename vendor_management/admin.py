from django.contrib import admin
from vendor_management.models import Vendor, PurchaseOrder, HistoricalPerformance
# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "contact_details", "address", "vendor_code", "on_time_delivery_rate",
                    "quality_rating_avg", "average_response_time", "fulfillment_rate"]
admin.site.register(Vendor,VendorAdmin)


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ["id", "po_number", "vendor", "order_date", "delivery_date", "items",
                    "quantity", "status", "quality_rating", "issue_date", "acknowledgment_date"]

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)


class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ["id", "vendor", "date", "on_time_delivery_rate", "quality_rating_avg", "average_response_time",
                    "fulfillment_rate"]
admin.site.register(HistoricalPerformance,HistoricalPerformanceAdmin)
