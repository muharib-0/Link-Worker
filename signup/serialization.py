from rest_framework import serializers

from signup.models import userprofile 

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = userprofile
        fields = ['id', 'username', 'email', 'password', 'role']