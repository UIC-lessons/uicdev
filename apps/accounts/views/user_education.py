from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.accounts.models import UserEducation
from apps.accounts.serializers import UserEducationSerializer


class UserEducationListCreateAPIView(ListCreateAPIView):
    queryset = UserEducation.objects.all()
    serializer_class = UserEducationSerializer


class UserEducationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserEducation.objects.all()
    serializer_class = UserEducationSerializer
