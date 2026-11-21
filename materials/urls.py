from django.urls import include, path
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessonListCreateAPIView, LessonRetrieveUpdateDestroyAPIView

router = DefaultRouter()
router.register("courses", CourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("lessons/", LessonListCreateAPIView.as_view()),
    path("lessons/<int:pk>/", LessonRetrieveUpdateDestroyAPIView.as_view(), name="lesson-detail"),
]
