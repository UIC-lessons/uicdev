from rest_framework.serializers import ModelSerializer
from apps.courses.models import Enrollment
from apps.accounts.serializers import UserSerializer
from apps.courses.serializers import CourseSerializer
from apps.courses.models import Course
from rest_framework.serializers import PrimaryKeyRelatedField

class EnrollmentSerializer(ModelSerializer):
    course = PrimaryKeyRelatedField(queryset=Course.objects.all())
    course = CourseSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Enrollment
        fields = [
            "id",
            "user",
            "course",
            "started_at",
            "finished_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "user", "created_at", "updated_at","finished_at"]
        lookup_field = "id"

    def create(self, validated_data):
        user = self.context["request"].user
        course = validated_data["course"]
        enrollment = Enrollment.objects.create(user=user, course=course)
        return enrollment

            