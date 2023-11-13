import pytest

from ...models import Car, CarImages
from ...serializers.car_serializer import CarSerializer


@pytest.mark.django_db
def test_car_serializer_create(car_request_data_with_images):
    serializer = CarSerializer(data=car_request_data_with_images, partial=True)
    assert serializer.is_valid()
    car_instance = serializer.save()
    assert Car.objects.filter(id=car_instance.id).exists()
    assert CarImages.objects.filter(car_id=car_instance.id).exists()


@pytest.mark.django_db
def test_car_serializer_update(car_data, car_request_data_with_images):
    car_request_data_with_images['car_id'] = car_data.pk
    car_instance = car_data

    serializer = CarSerializer(
        instance=car_instance, data=car_request_data_with_images, partial=True
    )
    if serializer.is_valid():
        car_instance = serializer.save()

    assert serializer.is_valid()

    car_instance.refresh_from_db()

    car_request_data_with_images = set(['image1', 'image2'])
    car_images = CarImages.objects.filter(car_id=car_instance)
    assert (
        set([image.name for image in car_images])
        == car_request_data_with_images
    )
