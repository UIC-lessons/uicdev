from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from apps.common.models import Media
from apps.common.serializers import MediaSerializer


class MediaListCreateAPIView(ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaDestroyAPIView(DestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

