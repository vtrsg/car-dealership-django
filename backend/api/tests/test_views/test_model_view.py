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

        response = viewset.retrieve(request, pk_model=model_type_data.id)

        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_model_not_found(request_func):
        viewset = ModelViewSet()
        invalid_model_id = 404

        request = request_func
        request.method = 'GET'

        response = viewset.retrieve(request, pk_model=invalid_model_id)

        assert response.status_code == status.HTTP_404_NOT_FOUND
