from rest_framework.serializers import ModelSerializer
from apps.courses.models import Module
from apps.courses.serializers import CourseSerializer

class ModuleSerializer(ModelSerializer):
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Module
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]