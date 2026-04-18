from rest_framework.serializers import ModelSerializer
from apps.common.models import City
from apps.common.serializers import CountrySerializer


class CitySerializer(ModelSerializer):
    country = CountrySerializer(read_only=True)
    class Meta:
        model = City
        fields = [
            "id",
            "name",
            "country",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        lookup_field = "id"
