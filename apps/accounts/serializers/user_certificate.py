from rest_framework.serializers import ModelSerializer
from apps.accounts.models import UserCertificate
from apps.accounts.serializers import UserSerializer
from apps.courses.serializers import CourseSerializer


class UserCertificateSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    class Meta:
        model = UserCertificate
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
