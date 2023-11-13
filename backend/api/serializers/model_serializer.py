from rest_framework import serializers

from ..models import ModelType


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelType
        fields = '__all__'
