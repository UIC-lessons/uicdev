from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.courses.models import LessonResource
from apps.courses.serializers import LessonResourceSerializer

class LessonResourceListCreateAPIView(ListCreateAPIView):
    queryset = LessonResource.objects.all()
    serializer_class = LessonResourceSerializer

class LessonResourceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LessonResource.objects.all()
    serializer_class = LessonResourceSerializer