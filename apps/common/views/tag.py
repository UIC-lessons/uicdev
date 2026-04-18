from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.common.models import Tag
from apps.common.serializers import TagSerializer


class TagListCreateAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer



class TagRetriveUpdateDetstroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

