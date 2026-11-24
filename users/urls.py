from django.urls import path

from users.views import PaymentListCreateAPIView

urlpatterns = [
    path("payments/", PaymentListCreateAPIView.as_view(), name="payments"),
]
