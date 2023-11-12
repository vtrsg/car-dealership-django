import pytest

from ...models import Brand
from ...serializers.brand_serializer import BrandSerializer


@pytest.mark.django_db
def test_brand_serializer():
    brand_data = {'name': 'Test Brand'}
    brand = Brand.objects.create(**brand_data)

    serializer = BrandSerializer(instance=brand)

    assert serializer.data['name'] == brand_data['name']
