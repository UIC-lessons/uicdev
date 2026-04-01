from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.interactions.models import LessonQuestion
from apps.interactions.serializers import LessonQuestionSerializer


class LessonQuestionListCreateAPIView(ListCreateAPIView):
    queryset = LessonQuestion.objects.all()
    serializer_class = LessonQuestionSerializer


class LessonQuestionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LessonQuestion.objects.all()
    serializer_class = LessonQuestionSerializer
