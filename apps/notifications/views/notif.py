from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from apps.notifications.models import Notification
from apps.notifications.serializers import NotificationSerializer


class NotificationListAPIView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationCreateAPIView(CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationUpdateAPIView(UpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationDeleteAPIView(DestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationRetrieveAPIView(RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    
