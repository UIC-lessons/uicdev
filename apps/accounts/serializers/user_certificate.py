from rest_framework.serializers import ModelSerializer
from apps.accounts.models import UserCertificate


class UserCertificateSerializer(ModelSerializer):
    class Meta:
        model = UserCertificate
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
