from django.db import models
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def update_performance_metrics(self):
        completed_orders = self.purchase_orders.filter(status='completed')
        total_completed_orders = completed_orders.count()
        if total_completed_orders > 0:
            on_time_orders = completed_orders.filter(delivery_date__lte=timezone.now())
            self.on_time_delivery_rate = (on_time_orders.count() / total_completed_orders) * 100
        else:
            self.on_time_delivery_rate = 0

        completed_orders_with_rating = completed_orders.exclude(quality_rating__isnull=True)
        total_completed_orders_with_rating = completed_orders_with_rating.count()
        if total_completed_orders_with_rating > 0:
            self.quality_rating_avg = completed_orders_with_rating.aggregate(models.Avg('quality_rating'))[
                'quality_rating__avg']
        else:
            self.quality_rating_avg = 0

        acknowledged_orders = completed_orders.exclude(acknowledgment_date__isnull=True)
        total_acknowledged_orders = acknowledged_orders.count()
        if total_acknowledged_orders > 0:
            total_response_time = sum(
                (order.acknowledgment_date - order.issue_date).total_seconds() for order in acknowledged_orders)
            self.average_response_time = total_response_time / total_acknowledged_orders
        else:
            self.average_response_time = 0

        successful_orders = completed_orders.exclude(issue_date__isnull=True)
        total_successful_orders = successful_orders.count()
        if total_completed_orders > 0:
            self.fulfillment_rate = (total_successful_orders / total_completed_orders) * 100
        else:
            self.fulfillment_rate = 0

        self.save()


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(default=timezone.now)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='historical_performance')
    date = models.DateTimeField(default=timezone.now)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor} - {self.date}"
