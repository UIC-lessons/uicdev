from rest_framework.serializers import ModelSerializer
from apps.accounts.models import UserEducation
from apps.accounts.serializers import UserSerializer
from apps.accounts.serializers import EducationSerializer


class UserEducationSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    education = EducationSerializer(read_only=True)
    class Meta:
        model = UserEducation
        fields = [
            "id",
            "user",
            "education",
            "field",
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
