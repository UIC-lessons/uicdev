from rest_framework import serializers
from django.core.validators import RegexValidator

class RegisterSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15, validators=[RegexValidator(r'^\+?[0-9]+$')])

    