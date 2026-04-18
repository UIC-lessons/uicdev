from rest_framework.serializers import ModelSerializer
from apps.courses.models import Course
from apps.courses.serializers import AuthorSerializer
from apps.common.serializers import CategorySerializer, MediaSerializer, TagSerializer


class CourseSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    banner = MediaSerializer(read_only=True)
    tags = TagSerializer(read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "description",
            "category",
            "author",
            "banner",
            "tags",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]