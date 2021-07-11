from rest_framework import serializers
from .models import AdminUser

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = ("name", "phone", "pincode")

class UpdateUserResultSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=255)
    result = serializers.BooleanField()