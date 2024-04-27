from rest_framework import serializers
from .models import User

# userlogin serializer.
class UserLogin_Serializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ["email", "password"]