from rest_framework.serializers import ModelSerializer
from apps.interactions.models import LessonRate


class LessonRateSerializer(ModelSerializer):
    class Meta:
        model = LessonRate
        fields = "__all__"
        read_only_fields = ["id", "lesson", "is_deleted", "created_at", "updated_at"]
        lookup_field = "id"
