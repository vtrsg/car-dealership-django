import re

from rest_framework import serializers
from rest_framework.validators import ValidationError

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone', 'cpf')

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
