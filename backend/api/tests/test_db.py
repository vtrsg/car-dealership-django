from pytest import mark

from api.models import Car


@mark.django_db
def test_create_user(user_data):
    user = user_data
    assert user.name == 'test user'
    assert user.email == 'test@testuser.com'
    assert user.phone == '51 9 9999-9999'
    assert user.cpf == '000.000.000-00'


@mark.django_db
def test_create_brand(brand_data):
    brand = brand_data
    assert brand.name == 'Mercedes'


@mark.django_db
def test_create_model_type(model_type_data):
    model = model_type_data
    assert model.name == 'SUV'


@mark.django_db
def test_create_year(year_data):
    year = year_data
    assert year.year == '2020'


@mark.django_db
def test_create_car(user_data, brand_data, model_type_data, year_data):
    car = Car.objects.create(
        user_id=user_data,
        name='Car Test',
        brand_id=brand_data,
        model_id=model_type_data,
        year_id=year_data,
        location=2,
        transmission=2,
        price=500000,
        discount_price=5000,
        mileage=125000,
        color='black',
        seat=5,
        fuel=2,
        image_file='https://localtest.com/image.jpg',
    )

    assert car.name == 'Car Test'
    assert car.location == 2
    assert car.transmission == 2
    assert car.price == 500000
    assert car.discount_price == 5000
    assert car.mileage == 125000
    assert car.color == 'black'
    assert car.seat == 5
    assert car.fuel == 2
    assert car.image_file == 'https://localtest.com/image.jpg'
