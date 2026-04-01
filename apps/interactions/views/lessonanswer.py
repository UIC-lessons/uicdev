from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.interactions.models import LessonAnswer
from apps.interactions.serializers import LessonAnswerSerializer


class LessonAnswerListCreateAPIView(ListCreateAPIView):
    queryset = LessonAnswer.objects.all()
    serializer_class = LessonAnswerSerializer


class LessonAnswerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LessonAnswer.objects.all()
    serializer_class = LessonAnswerSerializer
