from rest_framework import serializers

from ..models import ModelType


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelType
        fields = (
            'name',
            'brand_id',
            'year_id',
            'category',
        )

    def create(self, validated_data):
        name = validated_data['name']
        brand_id = validated_data['brand_id']
        year_id = validated_data['year_id']
        category = validated_data['category']

        model_type = ModelType.objects.get_or_create(
            name=name.upper(),
            brand_id=brand_id,
            year_id=year_id,
            category=category,
        )

        return model_type
