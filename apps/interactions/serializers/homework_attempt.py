from rest_framework.serializers import ModelSerializer
from apps.interactions.models import UserHomeworkAttempt


class UserHomeworkAttemptSerializer(ModelSerializer):
    class Meta:
        model = UserHomeworkAttempt
        fields = "__all__"
        read_only_fields = ["id", "lesson", "created_at", "updated_at"]
