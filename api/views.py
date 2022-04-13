from multiprocessing import managers
from smtpd import DebuggingServer
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
import datetime
from api.models import Company, User, UserHistory

from api.serializer import CompanySerializer, MyTokenObtainPairSerializer, UserHistorySerializor, UserSerializer


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
    serializer = UserSerializer(employee, many=True)

    return Response(serializer.data)
    # return JsonResponse("ok", safe=False)


@csrf_exempt
@api_view(['GET'])
def getComanyList(request):
    companies = Company.objects.all()
    serialized_companies = CompanySerializer(companies, many=True)
    return Response(serialized_companies.data)


def updateCurrCompany(request, pk, company=None):
    user = User.objects.filter(id=pk).update(
        curr_company=company, curr_join=datetime.date.today())
    return Response(user)


def addHistory(request, pk=None):
    user = User.objects.get(id=pk)
    serialized_user = UserSerializer(user)
    company = Company.objects.get(id=serialized_user.data['curr_company'])

    last_date = datetime.date.fromisoformat(serialized_user.data['curr_join'])
    duration = (datetime.date.today() - last_date).days

    serialized_history = UserHistorySerializor(UserHistory.objects.create(
        user=user, company=company, duration=duration,
    ))
    return Response(serialized_history.data)


# User leave the current company id in url via get metod
# User join the new company via company id in payload and post method


@ csrf_exempt
@ api_view(['GET', 'POST'])
def joinLeaveCompany(request, pk=None):
    if request.method == 'GET':
        addHistory(request._request, pk)
        return updateCurrCompany(request._request, pk)
    if request.method == 'POST':
        payload = request.data
        compamy = Company.objects.get(id=payload['id'])
        return updateCurrCompany(request._request, pk, compamy)


# User request his history of companies here
@ csrf_exempt
@ api_view(['GET'])
def userHistory(request, pk=None):
    history_list = UserHistory.objects.filter(user=pk)
    serialized_history_list = UserHistorySerializor(history_list, many=True)
    return Response(serialized_history_list.data)
