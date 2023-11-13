from rest_framework import serializers

from ..models import Car, CarImages


class CarSerializer(serializers.ModelSerializer):
    images = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])

        car = Car.objects.create(**validated_data)

        for image_data in images_data:
            image_name = f'{image_data["name"]}_{car.id}'
            image_url = image_data['image_url']
            CarImages.objects.create(
                car_id=car, image_url=image_url, name=image_name
            )

        return car

    def update(self, instance, validated_data):
        images_data = validated_data.get('images', [])
        for image_data in images_data:
            image_name = f'{image_data["name"]}'
            image_url = image_data['image_url']
            try:
                car_image = CarImages.objects.get(
                    car_id=instance, name=image_name
                )
                car_image.image_url = image_url
                car_image.save()
            except CarImages.DoesNotExist:
                CarImages.objects.create(
                    car_id=instance, image_url=image_url, name=image_name
                )

        return instance
