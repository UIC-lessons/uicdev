from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.accounts.models import UserExperience
from apps.accounts.serializers import UserExperienceSerializer


class UserExperienceListCreateAPIView(ListCreateAPIView):
    queryset = UserExperience.objects.all()
    serializer_class = UserExperienceSerializer


class UserExperienceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserExperience.objects.all()
    serializer_class = UserExperienceSerializer
