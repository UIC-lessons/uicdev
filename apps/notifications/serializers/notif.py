from apps.notifications.models import Notification
from rest_framework.serializers import ModelSerializer


class NotificationSerializer(ModelSerializer):
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
