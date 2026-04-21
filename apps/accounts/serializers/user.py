from rest_framework.serializers import ModelSerializer
from apps.accounts.models import User
from apps.common.serializers import MediaSerializer


class UserSerializer(ModelSerializer):
    avatar = MediaSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone",
            "bio",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
            "avatar"
        ]
        read_only_fields = (
            "id",
            "date_joined",
            "is_active",
            "is_staff",
            "is_superuser"
        )
        extra_kwargs = {
            "password": {"write_only": True}
    }
