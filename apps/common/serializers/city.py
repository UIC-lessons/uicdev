from rest_framework.serializers import ModelSerializer
from apps.common.models import City


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        lookup_field = "id"
