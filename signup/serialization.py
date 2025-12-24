from rest_framework import serializers

from signup.models import userprofile 

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = userprofile
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
    
        password = validated_data.pop('password')
        user = userprofile(**validated_data)
        user.set_password(password)
        user.save() 
        return user


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = userprofile
        fields = ['email', 'password']        