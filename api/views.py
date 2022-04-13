from multiprocessing import managers
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.models import User

from api.serializer import MyTokenObtainPairSerializer, UserSerializer


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@csrf_exempt
@api_view(['POST'])
def register(request):
    data = request.data
    employee = User.objects.create_user(
        data['email'], data['full_name'], data['password']
    )
    serializer = UserSerializer(employee)

    return Response(serializer.data)
    # return JsonResponse("ok", safe=False)
