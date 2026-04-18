from rest_framework.serializers import ModelSerializer
from apps.accounts.models import Education
from apps.accounts.serializers import UserSerializer


class EducationSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Education
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
