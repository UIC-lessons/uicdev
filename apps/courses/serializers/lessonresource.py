from rest_framework.serializers import ModelSerializer
from apps.courses.models import LessonResource

class LessonResourceSerializer(ModelSerializer):
    class Meta:
        model = LessonResource
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]