from django.urls import path
from apps.interactions.views import (
    UserHomeworkAttemptListCreateAPIView,
    UserHomeworkAttemptRetrieveUpdateDestroyAPIView,
    LessonAnswerListCreateAPIView,
    LessonAnswerRetrieveUpdateDestroyAPIView,
    LessonQuestionListCreateAPIView,
    LessonQuestionRetrieveUpdateDestroyAPIView,
    LessonRateListCreateAPIView,
    LessonRateRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("homework-attempt/", UserHomeworkAttemptListCreateAPIView.as_view()),
    path(
        "homework-attempt/<int:pk>/",
        UserHomeworkAttemptRetrieveUpdateDestroyAPIView.as_view(),
    ),
    path("lesson-answer/", LessonAnswerListCreateAPIView.as_view()),
    path(
        "lesson-answer/<int:pk>/",
        LessonAnswerRetrieveUpdateDestroyAPIView.as_view(),
    ),
    path("lesson-question/", LessonQuestionListCreateAPIView.as_view()),
    path(
        "lesson-question/<int:pk>/",
        LessonQuestionRetrieveUpdateDestroyAPIView.as_view(),
    ),
    path("lesson-rate/", LessonRateListCreateAPIView.as_view()),
    path(
        "lesson-rate/<int:pk>/",
        LessonRateRetrieveUpdateDestroyAPIView.as_view(),
    ),
]
