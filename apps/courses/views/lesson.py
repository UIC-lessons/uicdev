from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.courses.models import Lesson
from apps.courses.serializers import LessonSerializer

class LessonListCreateAPIView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer