from rest_framework.serializers import ModelSerializer
from apps.courses.models import Author

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]