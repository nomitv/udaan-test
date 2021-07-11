from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AdminUser
from .serializers import AdminUserSerializer, UpdateUserResultSerializer
from user.models import User
# Create your views here.

class AdminUserDetails(APIView):
    serializer_class = AdminUserSerializer

    def get_queryset(self):
        return AdminUser.objects.all()

    def get(self, request):
        try:
            queryset = AdminUser.objects.all()
            serializer = self.serializer_class(self.queryset, many=True)
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

class UpdateUserResult(APIView):
    serializer_class = UpdateUserResultSerializer

    def patch(self, request, id=None):
        try:
            if request.user in Admin.objects.all():
                user = User.objects.get(id=id)
                if serializer.is_valid():
                    user.result = serializer.validated_data['result']
                    user.save()
                    res = {}
                    res['updated'] = user.result
                    return Response(res, status=status.HTTP_200_OK)
            else:
                return Response("Only admin users can modify the result", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
