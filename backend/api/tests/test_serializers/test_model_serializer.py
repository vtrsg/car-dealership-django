import pytest

from ...models import ModelType
from ...serializers.model_serializer import ModelSerializer


@pytest.mark.django_db
def test_model_serializer():
    model_data = {'name': 'SUV'}
    model = ModelType.objects.create(**model_data)

    serializer = ModelSerializer(instance=model)

    assert serializer.data['name'] == model_data['name']
