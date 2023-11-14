import pytest

from api.models import Brand, Car, ModelType, User, Year


@pytest.fixture(autouse=True)
def user_data():
    user_data = User.objects.create(
        user_name='test user',
        first_name='test user',
        email='test@testuser.com',
        phone='51 9 9999-9999',
        cpf='000.000.000-00',
        password='123456789',
    )

    return user_data


@pytest.fixture(autouse=True)
def user_invalid_data():
    user_invalid_data = {
        'name': 'Test User',
        'email': 'test@example.com',
        'phone': 'invalid phone',
    }
    return user_invalid_data


@pytest.fixture(autouse=True)
def user_request_data():
    user_request_data = {
        'user_name': 'other test user',
        'first_name': 'other test user',
        'email': 'testother1@testuser.com',
        'phone': '+555199999-9999',
        'cpf': '030.450.000-01',
        'password': '123456789',
    }

    return user_request_data


@pytest.fixture(autouse=True)
def brand_data():
    brand_data = Brand.objects.create(name='Mercedes')

    return brand_data


@pytest.fixture(autouse=True)
def year_data():
    year_data = Year.objects.create(year='2020')

    return year_data


@pytest.fixture(autouse=True)
def model_type_data(brand_data, year_data):
    model_type_data = ModelType.objects.create(
        name='Kicks ADVANCE',
        category='SUV',
        brand_id=brand_data,
        year_id=year_data,
    )

    return model_type_data


@pytest.fixture(autouse=True)
def request_model_type_data(brand_data, year_data):
    request_model_type_data = {
        'name': 'Ecosport',
        'category': 'SUV',
        'brand_id': brand_data.pk,
        'year_id': year_data.pk,
    }

    return request_model_type_data


@pytest.fixture(autouse=True)
def request_invalid_model_type_data():
    request_invalid_model_type_data = {
        'name': 'Ecosport',
        'category': 'SUV',
        'brand_id': 50,
        'year_id': 30,
    }

    return request_invalid_model_type_data


@pytest.fixture(autouse=True)
def car_data(user_data, brand_data, model_type_data, year_data):
    car_data = Car.objects.create(
        name='car test 1',
        location=2,
        transmission=0,
        price=120000,
        discount_price=10000,
        mileage=500000,
        color='black',
        seat=5,
        fuel=0,
        activate=True,
        main_image='https://exemplo.com.br/image_test.png',
        user_id=user_data,
        brand_id=brand_data,
        model_id=model_type_data,
        year_id=year_data,
    )

    return car_data


@pytest.fixture(autouse=True)
def car_request_data(user_data, brand_data, model_type_data, year_data):
    car_request_data = {
        'name': 'car test 2',
        'location': 2,
        'transmission': 0,
        'price': 1500000,
        'discount_price': 5000,
        'mileage': 500000,
        'color': 'green',
        'seat': 5,
        'fuel': 0,
        'activate': True,
        'main_image': 'https://exemplo.com.br/image_test_2.png',
        'user_id': user_data.id,
        'brand_id': brand_data.id,
        'model_id': model_type_data.id,
        'year_id': year_data.id,
    }

    return car_request_data


@pytest.fixture(autouse=True)
def car_request_data_with_images(
    user_data, brand_data, model_type_data, year_data
):
    car_request_data_with_images = {
        'name': 'car test 3',
        'location': 2,
        'transmission': 0,
        'price': 1500000,
        'discount_price': 5000,
        'mileage': 500000,
        'color': 'green',
        'seat': 5,
        'fuel': 0,
        'activate': True,
        'main_image': 'https://exemplo.com.br/image_test_2.png',
        'user_id': user_data.id,
        'brand_id': brand_data.id,
        'model_id': model_type_data.id,
        'year_id': year_data.id,
        'images': [
            {'name': 'image1', 'image_url': 'https://example.com/image1.jpg'},
            {'name': 'image2', 'image_url': 'https://example.com/image2.jpg'},
        ],
    }

    return car_request_data_with_images


@pytest.fixture(autouse=True)
def car_invalid_request_data():
    car_invalid_request_data = {
        'name': 'car test 2',
        'location': 10,
        'transmission': 0,
        'price': 1500000,
        'discount_price': 5000,
        'mileage': 500000,
        'color': 'green',
        'seat': 5,
        'fuel': 300,
        'activate': True,
    }

    return car_invalid_request_data
