import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken

from ...models import User
from ...views.user_view import BlacklistTokenUpdateView, CustomUserCreate


@pytest.fixture
def request_func(user_request_data):
    factory = APIRequestFactory()
    request = factory.post(
        '/api/user/create/', data=user_request_data, format='json'
    )
    return request


@pytest.fixture
def authenticated_user():
    user = User.objects.create_user(
        user_name='test_user',
        first_name='test user',
        email='test@test.com',
        phone='51 9 9999-9999',
        cpf='010.020.030-40',
        password='123456789',
    )

    refresh_token = RefreshToken.for_user(user)
    return {'refresh_token': str(refresh_token)}


@pytest.fixture
def request_func_blacklist(authenticated_user):
    factory = APIRequestFactory()
    request = factory.post(
        '/api/logout/blacklist/',
        {'refresh_token': authenticated_user['refresh_token']},
    )
    return request


@pytest.fixture
def invalid_request_func_blacklist(authenticated_user):
    authenticated_user['refresh_token'] = 'invalid_refresh_token'
    factory = APIRequestFactory()
    request = factory.post(
        '/api/logout/blacklist/',
        {'refresh_token': authenticated_user['refresh_token']},
    )
    return request


@pytest.mark.django_db
class TestUserViews:
    def test_custom_user_create(self, request_func):
        view = CustomUserCreate.as_view()
        response = view(request_func)
        assert response.status_code == status.HTTP_201_CREATED

    def test_invalid_custom_user_create(self):
        request_func_invalid = {
            'name': 'Test invalid',
            'email': 'test@example.com',
            'phone': '51956235832',
            'cpf': 'invalid',
        }
        factory = APIRequestFactory()
        request = factory.post(
            '/api/user/create/', data=request_func_invalid, format='json'
        )
        view = CustomUserCreate.as_view()
        response = view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_blacklist_token_update_view(self, request_func_blacklist):
        view = BlacklistTokenUpdateView.as_view()
        response = view(request_func_blacklist)
        assert response.status_code == status.HTTP_205_RESET_CONTENT

    def test_blacklist_token_update_view_exception_handling(
        self, invalid_request_func_blacklist
    ):
        view = BlacklistTokenUpdateView.as_view()

        response = view(invalid_request_func_blacklist)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {
            'status': 'Error',
            'errors': 'Token is invalid or expired',
        }
