from django.urls import path

from .views import (
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
    EducationListCreateAPIView,
    EducationRetrieveUpdateDestroyAPIView,
    UserCertificateListCreateAPIView,
    UserCertificateRetrieveUpdateDestroyAPIView,
    UserEducationListCreateAPIView,
    UserEducationRetrieveUpdateDestroyAPIView,
    UserExperienceListCreateAPIView,
    UserExperienceRetrieveUpdateDestroyAPIView,
    SendSmsAPIView,
)

urlpatterns = [
    path("users/", UserListCreateAPIView.as_view()),
    path("users/<int:pk>/", UserRetrieveUpdateDestroyAPIView.as_view()),
    path("educations/", EducationListCreateAPIView.as_view()),
    path("educations/<int:pk>/", EducationRetrieveUpdateDestroyAPIView.as_view()),
    path("user-certificates/", UserCertificateListCreateAPIView.as_view()),
    path("user-certificates/<int:pk>/", UserCertificateRetrieveUpdateDestroyAPIView.as_view()),
    path("user-educations/", UserEducationListCreateAPIView.as_view()),
    path("user-educations/<int:pk>/", UserEducationRetrieveUpdateDestroyAPIView.as_view()),
    path("user-experiences/", UserExperienceListCreateAPIView.as_view()),
    path("user-experiences/<int:pk>/", UserExperienceRetrieveUpdateDestroyAPIView.as_view()),
    path("send-sms/", SendSmsAPIView.as_view()),
]
