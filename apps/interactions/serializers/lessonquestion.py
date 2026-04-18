from rest_framework.serializers import ModelSerializer
from apps.interactions.models import LessonQuestion
from apps.courses.serializers import LessonSerializer
from apps.accounts.serializers import UserSerializer

class LessonQuestionSerializer(ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = LessonQuestion
        fields = "__all__"
        read_only_fields = "id", "lesson", "created_at", "updated_at"
