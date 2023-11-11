import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory

from ...models import User
from ...views.user_view import UserViewSet


@pytest.fixture
def request_func():
    factory = APIRequestFactory()
    request = factory.get('/api/users/')
    return request


@pytest.mark.django_db
class TestUserViewSet:
    def test_list_users(self, request_func):
        viewset = UserViewSet()

        response = viewset.list(request_func)

        assert response.status_code == status.HTTP_200_OK

    def test_create_user_success(self, user_request_data, request_func):
        viewset = UserViewSet()

        request = request_func
        request.data = user_request_data
        response = viewset.create(request)

        assert response.status_code == status.HTTP_201_CREATED

    def test_create_user_invalid_data(self, user_invalid_data, request_func):
        viewset = UserViewSet()

        request = request_func
        request.data = user_invalid_data
        response = viewset.create(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_retrieve_user(request_func):
        viewset = UserViewSet()
        user = User.objects.create(
            name='test user',
            email='test@testuser.com',
            phone='51 9 9999-9999',
            cpf='000.000.001-02',
        )

        request = request_func
        request.method = 'GET'

        response = viewset.retrieve(request, pk_user=user.id)

        assert response.status_code == status.HTTP_200_OK

        assert response.data['id'] == user.id
        assert response.data['name'] == user.name
        assert response.data['email'] == user.email

    def test_retrieve_user_not_found(request_func):
        viewset = UserViewSet()
        invalid_user_id = 999

        request = request_func
        request.method = 'GET'

        response = viewset.retrieve(request, pk_user=invalid_user_id)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_user(user_data, user_request_data, request_func):
        viewset = UserViewSet()
        user = User.objects.create(
            name='test user',
            email='test@testuser.com',
            phone='51 9 9999-9999',
            cpf='000.000.001-02',
        )

        request = request_func
        request.method = 'PATCH'
        request.data = user_request_data

        response = viewset.update(request, pk_user=user.id)

        assert response.status_code == status.HTTP_200_OK

        assert response.data['status'] == 'Success'
        assert response.data['message'] == 'User updated successfully.'

    def test_update_user_not_found(request_func):
        viewset = UserViewSet()
        invalid_user_id = 999

        request = request_func
        request.method = 'PATCH'
        request.data = {}

        response = viewset.update(request, pk_user=invalid_user_id)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_user_invalid_data(
        user_data, request_func, user_invalid_data
    ):
        viewset = UserViewSet()
        user = User.objects.create(
            name='test user',
            email='test@testuser.com',
            phone='51 9 9999-9999',
            cpf='000.000.001-02',
        )

        request = request_func
        request.method = 'PATCH'
        request.data = user_invalid_data

        response = viewset.update(request, pk_user=user.id)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_destroy_user(user_data, request_func):
        viewset = UserViewSet()
        user = User.objects.create(
            name='test user',
            email='test@testuser.com',
            phone='51 9 9999-9999',
            cpf='000.000.001-02',
        )

        request = request_func
        request.method = 'DELETE'

        response = viewset.destroy(request, pk_user=user.id)

        assert response.status_code == status.HTTP_200_OK

        assert response.data['status'] == 'Success'
        assert (
            response.data['message'] == f'User {user.id} deleted successfully.'
        )


@pytest.mark.django_db
def test_destroy_user_not_found(request_func):
    viewset = UserViewSet()
    invalid_user_id = 999

    request = request_func
    request.method = 'DELETE'

    response = viewset.destroy(request, pk_user=invalid_user_id)
    assert response.status_code == status.HTTP_404_NOT_FOUND
