from rest_framework import generics, viewsets
from rest_framework.exceptions import PermissionDenied

from materials.models import Course, Lesson
from materials.permissions import CoursePermission, LessonPermission
from materials.serializers import CourseSerializer, LessonSerializer


class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [LessonPermission]

    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name="moderators").exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(course__owner=user)

    def perform_create(self, serializer):
        course = serializer.validated_data["course"]
        if course.owner != self.request.user:
            raise PermissionDenied("Нельзя создать урок в чужом курсе.")

        serializer.save()


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [LessonPermission]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [CoursePermission]

    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name="moderators").exists():
            return Course.objects.all()
        return Course.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
