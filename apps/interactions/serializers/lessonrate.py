from rest_framework.serializers import ModelSerializer
from apps.interactions.models import LessonRate
from apps.courses.serializers import LessonSerializer
from apps.accounts.serializers import UserSerializer


class LessonRateSerializer(ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = LessonRate
        fields = "__all__"
        read_only_fields = ["id", "lesson", "is_deleted", "created_at", "updated_at"]
        lookup_field = "id"
