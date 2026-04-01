from rest_framework.serializers import ModelSerializer
from apps.accounts.models import Education


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
