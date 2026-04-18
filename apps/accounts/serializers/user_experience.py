from rest_framework.serializers import ModelSerializer
from apps.accounts.models import UserExperience
from apps.accounts.serializers import UserSerializer


class UserExperienceSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserExperience
        fields = [
            "id",
            "user",
            "name",
            "position",
            "website_url",
            "skills",
            "start_date",
            "end_date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
