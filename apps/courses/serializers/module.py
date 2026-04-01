from rest_framework.serializers import ModelSerializer
from apps.courses.models import Module

class ModuleSerializer(ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]