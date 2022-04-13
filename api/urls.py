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
    # Leaving company needs to crate a userHistory record -> view supporting function /working
    # get the history of user where he had worked in the past /done
    path('user/register/', views.register, name='register-user'),
    path('user/<str:pk>/company/', views.joinLeaveCompany,
         name='join-leave-company'),
    path('user/<str:pk>/history/', views.userHistory, name='user-history'),



    # Gives the list of all companies /done
    path('company/all/', views.getComanyList, name='company-list'),





]
