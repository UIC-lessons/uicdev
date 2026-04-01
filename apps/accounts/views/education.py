from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.accounts.models import Education
from apps.accounts.serializers import EducationSerializer


class EducationListCreateAPIView(ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EducationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
