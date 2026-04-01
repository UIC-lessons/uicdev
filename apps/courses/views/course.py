from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.courses.models import Course
from apps.courses.serializers import CourseSerializer

class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer