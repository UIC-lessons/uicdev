from django.urls import path
from apps.common.views import (
    CountryAPIView,
    CityAPIView,
    TagListCreateAPIView,
    TagRetriveUpdateDetstroyAPIView,
    CategoryListCreateAPIView,
    CategoryRetriveUpdateDestroyAPIView,
    MediaDestroyAPIView,
    MediaListCreateAPIView,
)

urlpatterns = [
    path("country/", CountryAPIView.as_view(), name="countries"),
    path("country/<int:pk>/", CountryAPIView.as_view(), name="country"),
    path("city/", CityAPIView.as_view(), name="cities"),
    path("city/<int:pk>/", CityAPIView.as_view(), name="city"),
    path("category/", CategoryListCreateAPIView.as_view(), name="categories"),
    path(
        "category/<int:pk>/",
        CategoryRetriveUpdateDestroyAPIView.as_view(),
        name="category",
    ),
    path("tag/", TagListCreateAPIView.as_view(), name="tags"),
    path("tag/<int:pk>/", TagRetriveUpdateDetstroyAPIView.as_view(), name="tag"),
    path("media/", MediaListCreateAPIView.as_view(), name="media"),
    path("media/<int:pk>/", MediaDestroyAPIView.as_view(), name="media"),
]
