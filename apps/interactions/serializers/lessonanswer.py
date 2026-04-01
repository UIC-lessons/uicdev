from rest_framework.serializers import ModelSerializer
from apps.interactions.models import LessonAnswer


class LessonAnswerSerializer(ModelSerializer):
    class Meta:
        model = LessonAnswer
        fields = "__all__"
        read_only_fields = ["id", "lesson", "is_deleted", "created_at", "updated_at"]
        lookup_field = "id"
