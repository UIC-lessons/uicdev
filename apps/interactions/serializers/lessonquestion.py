from rest_framework.serializers import ModelSerializer
from apps.interactions.models import LessonQuestion


class LessonQuestionSerializer(ModelSerializer):
    class Meta:
        model = LessonQuestion
        fields = "__all__"
        read_only_fields = "id", "lesson", "created_at", "updated_at"
