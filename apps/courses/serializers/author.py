from rest_framework.serializers import ModelSerializer
from apps.courses.models import Author
from apps.accounts.serializers import UserSerializer
from apps.common.serializers import MediaSerializer

class AuthorSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    avatar = MediaSerializer(read_only=True)
    class Meta:
        model = Author
        fields = [
            "id",
            "user",
            "avatar",
            "first_name",
            "last_name",
            "description",
            "experience_years",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]