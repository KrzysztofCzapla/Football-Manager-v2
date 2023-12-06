from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.serializers import RegisterUserSerializer

class RegisterView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    @swagger_auto_schema(responses={status.HTTP_201_CREATED: "message"})
    def post(self, request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        if User.objects.filter(username__iexact=validated_data['username']).first() is not None:
            raise serializers.ValidationError("This username is already taken. Please choose a different one.")

        User.objects.create_user(username=validated_data['username'], password=validated_data['password'])

        return Response(
            status=status.HTTP_201_CREATED,
            data={"message": "User Registered Successfully"},
        )