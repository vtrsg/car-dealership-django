import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory

from ...views.model_view import ModelViewSet


@pytest.fixture
def request_func():
    factory = APIRequestFactory()
    request = factory.get('/api/models/')
    return request


@pytest.mark.django_db
class TestModelViewSet:
    def test_list_models(self, request_func):
        viewset = ModelViewSet()

        response = viewset.list(request_func)

        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_model(request_func, model_type_data):
        viewset = ModelViewSet()

        request = request_func
        request.method = 'GET'

        response = viewset.retrieve(request, pk_model=model_type_data.pk)

        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_model_not_found(request_func):
        viewset = ModelViewSet()
        invalid_model_id = 404

        request = request_func
        request.method = 'GET'

        response = viewset.retrieve(request, pk_model=invalid_model_id)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_create_model_success(self, request_model_type_data, request_func):
        viewset = ModelViewSet()

        request = request_func
        request.data = request_model_type_data
        response = viewset.create(request)

        assert response.status_code == status.HTTP_201_CREATED

    def test_create_model_invalid_data(
        self, request_invalid_model_type_data, request_func
    ):
        viewset = ModelViewSet()

        request = request_func
        request.data = request_invalid_model_type_data
        response = viewset.create(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_update_model(
        request_func, model_type_data, request_model_type_data
    ):
        viewset = ModelViewSet()
        request = request_func
        request.method = 'PATCH'
        request.data = request_model_type_data

        response = viewset.update(request, pk_model=model_type_data.pk)
        assert response.status_code == status.HTTP_200_OK

        assert response.data['status'] == 'Success'
        assert response.data['message'] == 'Model updated successfully.'

    def test_update_model_not_found(request_func):
        viewset = ModelViewSet()
        invalid_model_id = 404

        request = request_func
        request.method = 'PATCH'
        request.data = {}

        response = viewset.update(request, pk_model=invalid_model_id)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_model_invalid_data(
        request_func, model_type_data, request_invalid_model_type_data
    ):
        viewset = ModelViewSet()

        request = request_func
        request.method = 'PATCH'
        request.data = request_invalid_model_type_data

        response = viewset.update(request, pk_model=model_type_data.pk)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_destroy_model(request_func, model_type_data):
        viewset = ModelViewSet()
        request = request_func
        request.method = 'DELETE'

        response = viewset.destroy(request, pk_model=model_type_data.pk)

        assert response.status_code == status.HTTP_200_OK

        assert response.data['status'] == 'Success'
        assert (
            response.data['message']
            == f'Model {model_type_data.pk} deleted successfully.'
        )

    def test_destroy_model_not_found(request_func):
        viewset = ModelViewSet()
        invalid_model_id = 404

        request = request_func
        request.method = 'DELETE'

        response = viewset.destroy(request, pk_model=invalid_model_id)
        assert response.status_code == status.HTTP_404_NOT_FOUND
