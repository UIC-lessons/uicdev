from rest_framework.serializers import ModelSerializer
from apps.accounts.models import User
from apps.common.serializers import MediaSerializer


class UserSerializer(ModelSerializer):
    profile_picture = MediaSerializer(read_only=True)

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
            "profile_picture",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
        ]
        read_only_fields = (
            "id",
            "date_joined"
        )
        extra_kwargs = {
            "password": {"write_only": True}
    }
