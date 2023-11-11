import pytest

from api.models import Brand, ModelType, User, Year


@pytest.fixture
def user_data():
    user_data = User.objects.create(
        name='test user',
        email='test@testuser.com',
        phone='51 9 9999-9999',
        cpf='000.000.000-00',
    )

    return user_data


@pytest.fixture
def brand_data():
    brand_data = Brand.objects.create(name='Mercedes')

    return brand_data


@pytest.fixture
def model_type_data():
    model_type_data = ModelType.objects.create(name='SUV')

    return model_type_data


@pytest.fixture
def year_data():
    year_data = Year.objects.create(year='2020')

    return year_data
