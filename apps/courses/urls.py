from django.urls import path
from apps.courses.views import (
    AuthorListCreateAPIView,
    AuthorRetrieveUpdateDestroyAPIView,
    CourseListCreateAPIView,
    CourseRetrieveUpdateDestroyAPIView,
    EnrollmentListCreateAPIView,
    EnrollmentRetrieveUpdateDestroyAPIView,
    LessonListCreateAPIView,
    LessonRetrieveUpdateDestroyAPIView,
    LessonResourceListCreateAPIView,
    LessonResourceRetrieveUpdateDestroyAPIView,
    ModuleListCreateAPIView,
    ModuleRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("authors/", AuthorListCreateAPIView.as_view(), name="author-list-create"),
    path("authors/<int:pk>/", AuthorRetrieveUpdateDestroyAPIView.as_view(), name="author-retrieve-update-destroy"),
    path("courses/", CourseListCreateAPIView.as_view(), name="course-list-create"),
    path("courses/<int:pk>/", CourseRetrieveUpdateDestroyAPIView.as_view(), name="course-retrieve-update-destroy"),
    path("enrollments/", EnrollmentListCreateAPIView.as_view(), name="enrollment-list-create"),
    path("enrollments/<int:pk>/", EnrollmentRetrieveUpdateDestroyAPIView.as_view(), name="enrollment-retrieve-update-destroy"),
    path("lessons/", LessonListCreateAPIView.as_view(), name="lesson-list-create"),
    path("lessons/<int:pk>/", LessonRetrieveUpdateDestroyAPIView.as_view(), name="lesson-retrieve-update-destroy"),
    path("lesson-resources/", LessonResourceListCreateAPIView.as_view(), name="lesson-resource-list-create"),
    path("lesson-resources/<int:pk>/", LessonResourceRetrieveUpdateDestroyAPIView.as_view(), name="lesson-resource-retrieve-update-destroy"),
    path("modules/", ModuleListCreateAPIView.as_view(), name="module-list-create"),
    path("modules/<int:pk>/", ModuleRetrieveUpdateDestroyAPIView.as_view(), name="module-retrieve-update-destroy"),
]
