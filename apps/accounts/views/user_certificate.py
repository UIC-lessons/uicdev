from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.accounts.models import UserCertificate
from apps.accounts.serializers import UserCertificateSerializer


class UserCertificateListCreateAPIView(ListCreateAPIView):
    queryset = UserCertificate.objects.all()
    serializer_class = UserCertificateSerializer


class UserCertificateRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserCertificate.objects.all()
    serializer_class = UserCertificateSerializer
