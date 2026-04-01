from rest_framework.serializers import ModelSerializer
from apps.common.models import Country


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        lookup_field = "id"
