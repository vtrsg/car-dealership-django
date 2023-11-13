import pytest
from rest_framework.serializers import ValidationError

from ...serializers.user_serializer import UserSerializer


class TestUserSerializer:
    @pytest.fixture
    def user_data_serializer(self, user_data):
        return {
            'id': user_data.pk,
            'name': 'Test',
            'email': 'test@example.com',
            'phone': '51956235832',
            'cpf': '123.456.789-09',
        }

    @pytest.mark.django_db
    def test_user_serializer_is_valid(self, user_data_serializer):
        serializer = UserSerializer(data=user_data_serializer)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_user_serializer_save(self, user_data_serializer):
        serializer = UserSerializer(data=user_data_serializer)
        assert serializer.is_valid()

        user = serializer.save()

        assert user.name == user_data_serializer['name']
        assert user.email == user_data_serializer['email']
        assert user.phone == user_data_serializer['phone']
        assert user.cpf == '12345678909'

    @pytest.mark.django_db
    def test_user_serializer_invalid_cpf(self, user_data_serializer):
        user_data_serializer['cpf'] = 'invalid_cpf'
        serializer = UserSerializer(data=user_data_serializer)

        with pytest.raises(ValidationError, match='Invalid CPF number!!'):
            serializer.is_valid(raise_exception=True)
