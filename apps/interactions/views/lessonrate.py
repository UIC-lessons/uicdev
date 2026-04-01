from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.interactions.models import LessonRate
from apps.interactions.serializers import LessonRateSerializer


class LessonRateListCreateAPIView(ListCreateAPIView):
    queryset = LessonRate.objects.all()
    serializer_class = LessonRateSerializer


class LessonRateRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LessonRate.objects.all()
    serializer_class = LessonRateSerializer
