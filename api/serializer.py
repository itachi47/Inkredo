
from dataclasses import field, fields
from rest_framework.serializers import ModelSerializer
from .models import Company, User, UserHistory
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print("user:", user)
        token = super().get_token(user)

        # Add custom claims
        token['user_name'] = user.full_name
        # ...

        return token


class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserHistorySerializor(ModelSerializer):
    class Meta:
        model = UserHistory
        fields = '__all__'
