from rest_framework import serializers
from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['on_time_delivery_rate'] = instance.calculate_on_time_delivery_rate()
        data['quality_rating_avg'] = instance.calculate_quality_rating_average()
        data['average_response_time'] = instance.calculate_average_response_time()
        data['fulfillment_rate'] = instance.calculate_fulfillment_rate()
        return data
