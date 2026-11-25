from django.urls import path

from users.views import PaymentListCreateAPIView, UserCreateAPIView

urlpatterns = [
    path("payments/", PaymentListCreateAPIView.as_view(), name="payments"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
]
