from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import authentication
from clases import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from api import serializers, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.decorators import api_view



class UserViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.UserSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnUser,)
    filter_backends= (filters.SearchFilter,)
    search_fields= ('cnickname', 'cfirstname')

class UserLoginApiView(serializers.CustomAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.CountrySerializer
    queryset = models.Country.objects.all()

class CityViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.CitySerializer
    queryset = models.City.objects.all()

class GameViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.GameSerializer
    queryset = models.Game.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.CategorySerializer
    queryset = models.Category.objects.all()

class characteristic_userViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.characteristic_userSerializer
    queryset = models.characteristic_user.objects.all()    

class GenderViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.GenderSerializer
    queryset = models.Gender.objects.all()

class Detail_UserViewSet(viewsets.ModelViewSet):

    #@api_view(['GET'])
    #def detail_userList(request):
    #    queryset = models.detail_user.objects.all()
    #    serializer_class =serializers.Detail_UserSerializer(queryset, many=True)
    #    return Response(serializer_class.data)
#
    #@api_view(['POST'])
    #def detail_userCreate(request):
    #    serializer_class =serializers.Detail_UserSerializer(data=request.data)
#
    #    if serializer_class.is_valid():
    #        serializer_class.save()
#
    #    return Response(serializer_class.data)
    serializer_class =serializers.Detail_UserSerializer
    queryset = models.detail_user.objects.all()

class Detail_CategoryViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.Detail_CategorySerializer
    queryset = models.detail_category.objects.all()

class Detail_GameViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.Detail_GameSerializer
    queryset = models.detail_game.objects.all()