from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.interactions.models import UserHomeworkAttempt
from apps.interactions.serializers import UserHomeworkAttemptSerializer


class UserHomeworkAttemptListCreateAPIView(ListCreateAPIView):
    queryset = UserHomeworkAttempt.objects.all()
    serializer_class = UserHomeworkAttemptSerializer


class UserHomeworkAttemptRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserHomeworkAttempt.objects.all()
    serializer_class = UserHomeworkAttemptSerializer
