from rest_framework.serializers import ModelSerializer
from apps.interactions.models import UserHomeworkAttempt
from apps.courses.serializers import LessonSerializer
from apps.accounts.serializers import UserSerializer
from apps.common.serializers import MediaSerializer

class UserHomeworkAttemptSerializer(ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    work_file = MediaSerializer(read_only=True)
    class Meta:
        model = UserHomeworkAttempt
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
