from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
# import User.models as model
import userManagement.models as model
# from userManagement.serializers import *
from django.utils.timezone import now
from userManagement.serializers import *

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from userManagement.service import check_parameters

class Inscription(GenericAPIView,mixins.CreateModelMixin):
    serializer_class = UserSerializer
    permission_classes=[AllowAny]
    def post (self,request,*args, **kwargs):
        try:
            first_name=request.data['firstName']
            last_name=request.data['last_name']
            email=request.data['email']
            username=request.data['username']
            password=request.data['password']
            telephone=request.data['telephone']
            checkParamater=check_parameters(first_name,last_name,email,username,password,telephone)
            if checkParamater is True:
                findEmail=model.userApp.objects.filter(email=email).exists()
                findUserName=model.userApp.objects.filter(username=username).exists()
                if  not findEmail and not findUserName :
                     serializerUser = self.get_serializer(data=request.data)
                     instance =serializerUser.save()
                     token, _ = Token.objects.get_or_create(user=instance)
                     instance.auth_token = token.key
                     instance.save()
                     return Response(
                    data={"Message": "Thanks for signing up, "
                          "you can go to the login page",
                           'user': serializerUser.data,
                          'token': token.key},
                    status=status.HTTP_200_OK)
                else:
                       return Response(
                        data={
                            "Message": "You are already sign up, return to "
                            "sign in page"},
                        status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
             return Response(data={
                  "Message":str(e)},
                  status=status.HTTP_400_BAD_REQUEST

             )
                 
class LoginView(GenericAPIView):
    """Login"""
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    def post(self ,request):
         
             """Post"""
             req = JSONParser().parse(request)
             username = request.data.get('username')
             password = request.data.get('password')
             try:
                user = authenticate(username=username, password=password)
                if user:
                     return Response({'token': user.auth_token.key}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
             except Exception as e:
                    raise serializers.ValidationError("Invalid email address: " + str(e))
class LogoutView(GenericAPIView):
    """
    Logout
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            token = RefreshToken(request.data.get("refresh"))
            user = model.userApp.objects.get(id=request.user.id)
            data = now() - user.last_login
            data_time = data.total_seconds() / 3600
            user.last_logout = now()
            user.save()
            token.blacklist()
            return Response(
                data={"Message": "Logged out"},
                status=status.HTTP_204_NO_CONTENT)
        except Exception as e:

            return Response(
                data={"Message": str(e)},
                status=status.HTTP_400_BAD_REQUEST)
# class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

#     return Response("hello")