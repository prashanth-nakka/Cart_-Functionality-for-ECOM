from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class RegisterView(APIView):
    def post(self, request, format=None):
        username = request.data['username']
        password = request.data['password']
        user = User(username=username)
        user.set_password(password)
        user.save()
        token = RefreshToken.for_user(user)
        return Response(
            {"status": "success",
             "user_id": user.id,
             "user_name": user.username,
             "Refresh": str(token),
             "access": str(token.access_token)
            }
        )
