from rest_framework import serializers
from django.utils import timezone
from vendor_management.models import Vendor, PurchaseOrder, HistoricalPerformance


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        extra_kwargs = {
            'on_time_delivery_rate': {'read_only': True},
            'quality_rating_avg': {'read_only': True},
            'average_response_time': {'read_only': True},
            'fulfillment_rate': {'read_only': True},
        }

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    def validate(self, data):
        quantity = data.get('quantity')
        if quantity is not None and quantity <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0.")

        order_date = data.get('order_date')
        if order_date and order_date <= timezone.now():
            raise serializers.ValidationError("Order date must be in the future.")

        return data

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'