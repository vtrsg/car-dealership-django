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


# @pytest.fixture(autouse=True)
# def user_data_view():
#     user_data_view = User.objects.create(
#         name='test user',
#         email='test@test2user.com',
#         phone='51 9 9999-9999',
#         cpf='000.000.030-12',
#     )
#     return user_data_view
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

    def test_retrieve_user(request_func, user_data):
        viewset = UserViewSet()

        request = request_func
        request.method = 'GET'

        response = viewset.retrieve(request, pk_user=user_data.pk)

        assert response.status_code == status.HTTP_200_OK

        assert response.data['id'] == user_data.pk
        assert response.data['name'] == user_data.name
        assert response.data['email'] == user_data.email

    def test_retrieve_user_not_found(request_func):
        viewset = UserViewSet()
        invalid_user_id = 999

        request = request_func
        request.method = 'GET'

        response = viewset.retrieve(request, pk_user=invalid_user_id)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_user(request_func):
        viewset = UserViewSet()
        user_data_view = User.objects.create(
            name='test uuser',
            email='test@test10user.com',
            phone='5199999-9999',
            cpf='200.000.300-12',
        )
        user_request = {
            'name': 'other test user update',
        }
        request = request_func
        request.method = 'PATCH'
        request.data = user_request

        response = viewset.update(request, pk_user=user_data_view.pk)
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
        user_data_view = User.objects.create(
            name='test user',
            email='test@tes8user.com',
            phone='51 9 9999-9999',
            cpf='000.500.300-12',
        )
        request = request_func
        request.method = 'PATCH'
        request.data = user_invalid_data

        response = viewset.update(request, pk_user=user_data_view.pk)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_destroy_user(request_func):
        viewset = UserViewSet()
        user_data_view = User.objects.create(
            name='test user',
            email='test@test00user.com',
            phone='51 9 9999-9999',
            cpf='000.100.300-12',
        )
        request = request_func
        request.method = 'DELETE'

        response = viewset.destroy(request, pk_user=user_data_view.pk)

        assert response.status_code == status.HTTP_200_OK

        assert response.data['status'] == 'Success'
        assert (
            response.data['message']
            == f'User {user_data_view.pk} deleted successfully.'
        )

    def test_destroy_user_not_found(request_func):
        viewset = UserViewSet()
        invalid_user_id = 999

        request = request_func
        request.method = 'DELETE'

        response = viewset.destroy(request, pk_user=invalid_user_id)
        assert response.status_code == status.HTTP_404_NOT_FOUND
