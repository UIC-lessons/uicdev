from rest_framework.serializers import ModelSerializer
from apps.courses.models import Lesson

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]