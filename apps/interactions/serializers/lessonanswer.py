from rest_framework.serializers import ModelSerializer
from apps.interactions.models import LessonAnswer
from apps.accounts.serializers import UserSerializer
from apps.courses.serializers import LessonSerializer

class LessonAnswerSerializer(ModelSerializer):
    user = UserSerializer(read_only = True)
    lesson = LessonSerializer(read_only = True)
    class Meta:
        model = LessonAnswer
        fields = "__all__"
        read_only_fields = ["id", "lesson", "is_deleted", "created_at", "updated_at"]
        lookup_field = "id"
