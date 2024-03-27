from rest_framework import serializers
# from Usermangement.models import userApp
from userManagement.models import userApp

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=userApp
        fields="__all__"
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model =userApp
        fields = ("id", "username", "password")