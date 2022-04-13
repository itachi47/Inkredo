from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
from pickle import GET
from secrets import token_urlsafe
from sys import api_version
from django.urls import path


urlpatterns = [
    # Login and access tokens
    #     1. Login and access token    /done
    #     2. Refreshing the token      /done

    path('token/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),  # done
    path('token/refresh/', views.TokenRefreshView.as_view(),
         name='token_refresh'),  # done

    # register new user /done
    # join and leave current company /done
    # @supporting -> Leaving company needs to crate a userHistory record /done
    # get the history of user where he had worked in the past /done
    path('user/register/', views.register, name='register-user'),
    path('user/<str:pk>/company/', views.joinLeaveCompany,
         name='join-leave-company'),
    path('user/<str:pk>/history/', views.userHistory, name='user-history'),



    # Gives the list of all companies /done
    # Gives the list of present employee of the company /done
    # @supporting -> if emp leaves add to past list and remove from present /working
    # @supporting -> if emp join and was in pas change to present if not in present /present
    # Gives the list of past employee of the company /done
    path('company/all/', views.getComanyList, name='company-list'),
    path('company/<str:pk>/presentemployee/',
         views.getPresentEmployeeList, name='present-employee-list'),
    path('company/<str:pk>/pastemployee/',
         views.getPastEmployeeList, name='past-employee-list'),


]
