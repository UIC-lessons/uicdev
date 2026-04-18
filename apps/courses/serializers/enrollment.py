from rest_framework.serializers import ModelSerializer
from apps.courses.models import Enrollment
from apps.accounts.serializers import UserSerializer
from apps.courses.serializers import CourseSerializer

class EnrollmentSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Enrollment
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]