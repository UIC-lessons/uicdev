from django.urls import path
from apps.notifications.views import (
    NotificationListAPIView,
    NotificationCreateAPIView,
    NotificationUpdateAPIView,
    NotificationDeleteAPIView,
    NotificationRetrieveAPIView,
)

urlpatterns = [
    path("get/", NotificationListAPIView.as_view(), name="list"),
    path("create/", NotificationCreateAPIView.as_view(), name="create"),
    path("update/<int:pk>/", NotificationUpdateAPIView.as_view(), name="update"),
    path("delete/<int:pk>/", NotificationDeleteAPIView.as_view(), name="delete"),
    path("get/<int:pk>/", NotificationRetrieveAPIView.as_view(), name="retrieve"),
]
