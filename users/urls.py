from django.urls import path

from users.views import PaymentListCreateAPIView, UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("payments/", PaymentListCreateAPIView.as_view(), name="payments"),
    path("register/", UserListCreateAPIView.as_view(), name="register"),
    path("", UserListCreateAPIView.as_view(), name="user-list"),
    path("<int:pk>/", UserRetrieveUpdateDestroyAPIView.as_view(), name="user-detail"),
]
