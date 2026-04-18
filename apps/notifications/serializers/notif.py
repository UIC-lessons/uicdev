from apps.notifications.models import Notification
from rest_framework.serializers import ModelSerializer
from apps.accounts.serializers import UserSerializer
from apps.courses.serializers import CourseSerializer, ModuleSerializer
from apps.common.serializers import CategorySerializer, MediaSerializer

class NotificationSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    module = ModuleSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    image = MediaSerializer(read_only=True)
    class Meta:
        model = Notification
        fields = [
            "user",
            "course",
            "module",
            "category",
            "id",
            "title",
            "message",
            "is_send_to_all",
            "image",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "user",
            "course",
            "module",
            "category",
            "id",
            "image",
            "created_at",
            "updated_at",
        ]
        lookup_field = "id"
