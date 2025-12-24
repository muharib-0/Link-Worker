# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialization import SignupSerializer
from .models import userprofile
from django.contrib.auth.hashers import check_password
# Create your views here.
class signupview(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def get(self, request):
        users = userprofile.objects.all()
        serializer = SignupSerializer(users, many=True)
        return Response(serializer.data)    
    
class loginview(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        try:
            user=userprofile.objects.get(email=email)
            if check_password(password, user.password):
                return Response({"message": f"Login successful! Welcome back, {user.username}."},status=200)
            else:
                return Response({"message":"invalid credentials"},status=401)
        except userprofile.DoesNotExist:
            return Response({"message":"user not found"},status=404)

    