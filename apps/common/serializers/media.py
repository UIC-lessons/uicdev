from rest_framework.serializers import ModelSerializer
from apps.common.models import Media


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        lookup_field = "url"
