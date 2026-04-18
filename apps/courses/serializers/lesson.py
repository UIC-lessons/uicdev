from rest_framework.serializers import ModelSerializer
from apps.courses.models import Lesson
from apps.courses.serializers.module import ModuleSerializer
from apps.common.serializers import MediaSerializer

class LessonSerializer(ModelSerializer):
    module = ModuleSerializer(read_only = True)
    video = MediaSerializer(read_only = True)
    class Meta:
        model = Lesson
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]