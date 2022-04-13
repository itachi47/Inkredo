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





]
