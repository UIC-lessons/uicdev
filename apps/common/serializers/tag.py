from rest_framework.serializers import ModelSerializer
from apps.common.models import Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        lookup_field = "id"
