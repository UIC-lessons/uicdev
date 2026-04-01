from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.courses.models import Author
from apps.courses.serializers import AuthorSerializer

class AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer