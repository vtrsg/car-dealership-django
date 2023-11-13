import pytest
from rest_framework.serializers import ValidationError

from ...serializers.user_serializer import UserSerializer


class TestUserSerializer:
    @pytest.fixture
    def user_data(self):
        return {
            'name': 'Test',
            'email': 'test@example.com',
            'phone': '51956235832',
            'cpf': '123.456.789-09',
        }

    @pytest.mark.django_db
    def test_user_serializer_is_valid(self, user_data):
        serializer = UserSerializer(data=user_data)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_user_serializer_save(self, user_data):
        serializer = UserSerializer(data=user_data)
        assert serializer.is_valid()

        user = serializer.save()

        assert user.name == user_data['name']
        assert user.email == user_data['email']
        assert user.phone == user_data['phone']
        assert user.cpf == '12345678909'

    @pytest.mark.django_db
    def test_user_serializer_invalid_cpf(self, user_data):
        user_data['cpf'] = 'invalid_cpf'
        serializer = UserSerializer(data=user_data)

        with pytest.raises(ValidationError, match='Invalid CPF number!!'):
            serializer.is_valid(raise_exception=True)
