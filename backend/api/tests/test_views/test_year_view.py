import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory

from ...views.year_view import YearViewSet


@pytest.fixture
def request_func():
    factory = APIRequestFactory()
    request = factory.get('/api/years/')
    return request


@pytest.mark.django_db
class TestYearViewSet:
    def test_list_years(self, request_func):
        viewset = YearViewSet()

        response = viewset.list(request_func)

        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_year(request_func, year_data):
        viewset = YearViewSet()

        request = request_func
        request.method = 'GET'

        response = viewset.retrieve(request, pk_year=year_data.id)

        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_year_not_found(request_func):
        viewset = YearViewSet()
        invalid_year_id = 4040

        request = request_func
        request.method = 'GET'

        response = viewset.retrieve(request, pk_year=invalid_year_id)

        assert response.status_code == status.HTTP_404_NOT_FOUND
