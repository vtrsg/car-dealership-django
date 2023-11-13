import pytest

from ...models import Year
from ...serializers.year_serializer import YearSerializer


@pytest.mark.django_db
def test_year_serializer():
    year_data = {'year': '2020'}
    year = Year.objects.create(**year_data)

    serializer = YearSerializer(instance=year)

    assert serializer.data['year'] == year_data['year']
