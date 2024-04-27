from django.shortcuts import render
from .models import User
from blog.render import UserRenderer
from .serializer import UserLogin_Serializer
from django.contrib.auth import authenticate
from rest_framework import status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


# generating the token for the user.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

# user login view.
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLogin_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                uid = user.id
                token = get_tokens_for_user(user)
                return Response(
                    {
                        "token": token,
                        "msg": "Login Successfully",
                        "id": uid,
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"msg": "Email or Password is not valide"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

