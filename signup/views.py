from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialization import SignupSerializer
from .models import userprofile
# Create your views here.
class signupview(APIView):
    def post(self, request):
        # user=userprofile.objects.all()
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def get(self, request):
        users = userprofile.objects.all()
        serializer = SignupSerializer(users, many=True)
        return Response(serializer.data)    
    
    