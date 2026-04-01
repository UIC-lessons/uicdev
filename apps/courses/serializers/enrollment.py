from rest_framework.serializers import ModelSerializer
from apps.courses.models import Enrollment

class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]