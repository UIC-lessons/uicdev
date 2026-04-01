from rest_framework.serializers import ModelSerializer
from apps.accounts.models import UserExperience


class UserExperienceSerializer(ModelSerializer):
    class Meta:
        model = UserExperience
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
