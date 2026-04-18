from rest_framework.serializers import ModelSerializer
from apps.courses.models import LessonResource
from apps.courses.serializers import LessonSerializer
from apps.common.serializers import MediaSerializer

class LessonResourceSerializer(ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    media = MediaSerializer(read_only=True)
    class Meta:
        model = LessonResource
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]