from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import Payment

User = get_user_model()

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "password",)
        read_only_fields = ("id",)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(email=validated_data.pop("email"), password=password)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.item():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)

        instance.save()
        return instance