from rest_framework import serializers
from .models import User
from .models import OTP 

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password', 'age', 'gender')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user

from rest_framework import serializers
from .models import OTP, User
from django.utils import timezone
from datetime import timedelta

class RequestOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def create(self, validated_data):
        user = User.objects.get(email=validated_data['email'])
        otp_instance = OTP.objects.create(user=user)
        otp_instance.send_otp()
        return otp_instance


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data['email']
        otp = data['otp']
        try:
            otp_record = OTP.objects.get(user__email=email, otp=otp)
            # Optionally, you can add checks for expiration here
        except OTP.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP or email.")
        
        data['user'] = otp_record.user  # Attach the user to the validated data
        return data