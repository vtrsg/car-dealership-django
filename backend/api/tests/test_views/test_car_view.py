import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory

from ...views.car_view import CarViewSet


@pytest.fixture
def request_func():
    factory = APIRequestFactory()
    request = factory.get('/api/cars/')
    return request


@pytest.mark.django_db
class TestCarViewSet:
    def test_list_cars(self, request_func):
        viewset = CarViewSet()

        response = viewset.list(request_func)

        assert response.status_code == status.HTTP_200_OK

    def test_create_car_success(self, car_request_data, request_func):
        viewset = CarViewSet()

        request = request_func
        request.data = car_request_data
        response = viewset.create(request)
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_car_invalid_data(
        self, car_invalid_request_data, request_func
    ):
        viewset = CarViewSet()

        request = request_func
        request.data = car_invalid_request_data
        response = viewset.create(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_retrieve_car(request_func, car_data):
        viewset = CarViewSet()

        request = request_func
        request.method = 'GET'

        response = viewset.retrieve(request, pk_car=car_data.id)

        assert response.status_code == status.HTTP_200_OK

        assert response.data['id'] == car_data.id
        assert response.data['name'] == car_data.name

    def test_retrieve_car_not_found(request_func):
        viewset = CarViewSet()
        invalid_car_id = 404

        request = request_func
        request.method = 'GET'

        response = viewset.retrieve(request, pk_car=invalid_car_id)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_car(request_func, car_data):
        viewset = CarViewSet()
        car_request_data_update = {
            'name': 'car test 2',
            'location': 2,
        }
        request = request_func
        request.method = 'PATCH'
        request.data = car_request_data_update

        response = viewset.update(request, pk_car=car_data.id)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['status'] == 'Success'
        assert response.data['message'] == 'Car updated successfully.'

    def test_update_car_not_found(request_func):
        viewset = CarViewSet()
        invalid_car_id = 404

        request = request_func
        request.method = 'PATCH'
        request.data = {}

        response = viewset.update(request, pk_car=invalid_car_id)

        assert response.status_code == status.HTTP_404_NOT_FOUND
