from rest_framework.serializers import ModelSerializer
from apps.accounts.models import UserEducation


class UserEducationSerializer(ModelSerializer):
    class Meta:
        model = UserEducation
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
