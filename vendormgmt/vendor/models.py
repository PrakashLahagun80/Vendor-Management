from django.db import models
from django.utils import timezone


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.name

    def calculate_on_time_delivery_rate(self):
        completed_pos = self.purchaseorder_set.filter(status='completed')
        on_time_delivery_pos = completed_pos.filter(delivery_date__lte=timezone.now())
        total_completed_pos = completed_pos.count()

        if total_completed_pos == 0:
            return 0

        return on_time_delivery_pos.count() / total_completed_pos * 100

    def calculate_quality_rating_average(self):
        completed_pos_with_rating = self.purchaseorder_set.filter(status='completed', quality_rating__isnull=False)
        total_completed_pos = completed_pos_with_rating.count()

        if total_completed_pos == 0:
            return 0

        quality_ratings_sum = completed_pos_with_rating.aggregate(models.Sum('quality_rating'))['quality_rating__sum']
        return quality_ratings_sum / total_completed_pos

    def calculate_average_response_time(self):
        acknowledged_pos = self.purchaseorder_set.filter(status='acknowledged')
        total_acknowledged_pos = acknowledged_pos.count()

        if total_acknowledged_pos == 0:
            return None

        total_response_time = sum((po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledged_pos)
        return total_response_time / total_acknowledged_pos

    def calculate_fulfillment_rate(self):
        completed_pos = self.purchaseorder_set.filter(status='completed')
        successful_fulfillment_pos = completed_pos.exclude(quality_rating__isnull=False).count()
        total_pos = self.purchaseorder_set.count()

        if total_pos == 0:
            return 0

        return successful_fulfillment_pos / total_pos * 100
