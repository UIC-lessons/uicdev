from .country import CountryAPIView
from .city import CityListCreateAPIView, CityDetailAPIView
from .category import CategoryListCreateAPIView, CategoryRetriveUpdateDestroyAPIView
from .tag import TagListCreateAPIView, TagRetriveUpdateDetstroyAPIView
from .media import MediaListCreateAPIView, MediaDestroyAPIView

__all__ = [
    "CountryAPIView",
    "CityListCreateAPIView",
    "CityDetailAPIView",
    "CategoryListCreateAPIView",
    "CategoryRetriveUpdateDestroyAPIView",
    "TagListCreateAPIView",
    "TagRetriveUpdateDetstroyAPIView",
    "MediaListCreateAPIView",
    "MediaDestroyAPIView",
]
