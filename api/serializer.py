
from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Company, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print("user:", user)
        token = super().get_token(user)

        # Add custom claims
        token['user_name'] = user.full_name
        # ...

        return token
