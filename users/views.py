from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.permissions import AllowAny

from users.models import Payment
from users.serializers import PaymentSerializer, UserSerializer


class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ("payment_date", "course", "lesson", "payment_method")
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ("payment_date",)
    ordering = ("-payment_date",)


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
