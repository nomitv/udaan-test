from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "phone", "pincode")

class UserAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('contact_with_covid', 'travel_history', 'symptoms')

class ZoneSerializer(serializers.Serializer):
    pincode = serializers.CharField(max_length=6, min_length=6)