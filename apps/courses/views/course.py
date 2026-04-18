from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.courses.models import Course
from apps.courses.serializers import CourseSerializer

class CourseListCreateAPIView(ListCreateAPIView):
    serializer_class = CourseSerializer
    
    def get_queryset(self):
        queryset = (
            Course.objects.filter(is_active=True)
            .select_related(
                "author",
                "category",
                "banner",
            )
            .prefetch_related(
                "tags",
            )
            .order_by("name")
        )
        return queryset

class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = (
            Course.objects.filter(is_active=True)
            .select_related(
                "author",
                "category",
                "banner",
            )
            .prefetch_related(
                "tags",
            )
            .order_by("name")
        )
        return queryset