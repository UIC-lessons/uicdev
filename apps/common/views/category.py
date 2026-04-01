from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.common.models import Category
from apps.common.serializers import CategorySerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"
