from rest_framework.serializers import ModelSerializer
from apps.common.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
