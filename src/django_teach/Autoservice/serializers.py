from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
        exclude = ('is_active', 'created_at', 'updated_at')
        read_only_fields = ('id',)
