from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, RequestOTPSerializer, VerifyOTPSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]  # This allows unauthenticated users to register

    serializer_class = RegisterSerializer


class RequestOTPView(APIView):
    permission_classes = [AllowAny]  # This allows unauthenticated users to register
    def post(self, request):
        serializer = RequestOTPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "OTP sent to email."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    permission_classes = [AllowAny]  # This allows unauthenticated users to register
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "OTP verified. Login successful."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
