from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, UserAssessmentSerializer, ZoneSerializer
# Create your views here.

class UserDetails(APIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def get(self, request):
        try:
            queryset = User.objects.all()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_200_OK)

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class UserAssessment(APIView):
    serializer_class = UserAssessmentSerializer

    def patch(self, request, id=None):
        try:
            context = User.objects.get(id=id)
            serializer = self.serializer_class(context, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                user = User.objectsa.get(id=id)
                symptoms_length = len(user.symptoms)
                travel_history = user.travel_history
                contact_with_covid = user.contact_with_covid
                if symptoms_length == 0 and travel_history == False and contact_with_covid == False:
                    riskPercentage = 5
                elif symptoms_length == 1 and travel_history == True and contact_with_covid == True: 
                    riskPercentage = 50
                elif symptoms_length == 2 and travel_history == True and contact_with_covid == True: 
                    riskPercentage = 75
                elif symptoms_length > 2 and travel_history == True and contact_with_covid == True: 
                    riskPercentage = 95
                res = {}
                res['riskPercentage'] = riskPercentage
                return Response(res, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class GetZoneDetails(APIView):
    serializer_class = ZoneSerializer

    def get(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                pincode = serializer.validated_data['pincode']
                total_zones = User.objects.filter(pincode=pincode)
                positive_cases = 0
                for i in total_zones:
                    if i.result == True:
                        positive_cases += 1
                res = "GREEN"
                if positive_cases > 5:
                    res = "RED"
                elif positive_cases < 5:
                    res = "ORANGE"
                return Response(res, status=status.HTTP_200_OK)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)