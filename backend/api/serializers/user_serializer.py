import re

from rest_framework import serializers
from rest_framework.validators import ValidationError

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'user_name', 'password', 'phone', 'cpf')

    def validate_cpf(self, cpf):
        cpf_regex = re.compile(r'[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}')
        if not cpf_regex.match(cpf):
            raise ValidationError('Invalid CPF number!!')

        cpf = cpf.replace('.', '').replace('-', '')

        return cpf

    def validate_phone(self, phone):
        phone_regex = re.compile(
            r'(?:(?:\+|00)?(55)\s?)?(?:\(?([1-9][0-9])\)?\s?)(?:((?:9\d|[2-9])\d{3})\-?(\d{4}))'
        )
        if not phone_regex.match(phone):
            raise ValidationError('Invalid phone number!!')
        return phone

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
