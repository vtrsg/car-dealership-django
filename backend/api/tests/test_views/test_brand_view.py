import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory

from ...views.brand_view import BrandViewSet


@pytest.fixture
def request_func():
    factory = APIRequestFactory()
    request = factory.get('/api/brands/')
    return request


@pytest.mark.django_db
class TestBrandViewSet:
    def test_list_brands(self, request_func):
        viewset = BrandViewSet()

        response = viewset.list(request_func)

        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_brand(request_func, brand_data):
        viewset = BrandViewSet()

        request = request_func
        request.method = 'GET'

        response = viewset.retrieve(request, pk_brand=brand_data.id)

        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_brand_not_found(request_func):
        viewset = BrandViewSet()
        invalid_brand_id = 404

        request = request_func
        request.method = 'GET'

        response = viewset.retrieve(request, pk_brand=invalid_brand_id)

        assert response.status_code == status.HTTP_404_NOT_FOUND
