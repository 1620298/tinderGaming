from re import A, S
from django.contrib.auth.password_validation import password_changed
from django.db.models import fields
from rest_framework import serializers
from rest_framework.mixins import RetrieveModelMixin
from clases import models
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from base64 import b64encode



class UserSerializer(serializers.ModelSerializer):
    """serializa Usuario"""

    class Meta:
        model= models.User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }



    def create(self, validated_data):
        """crear y retornar nuevo usuario"""
        user = models.User.objects.create_user(
            cnickname = validated_data['cnickname'],
            password = validated_data['password'],
            cfirstname = validated_data['cfirstname'],
            clastname = validated_data['clastname'],
            dbirthdate = validated_data['dbirthdate'],
            cmail = validated_data['cmail'],
            cavatar = validated_data['cavatar'],
            cphone = validated_data['cphone'],
            clongitude = validated_data['clongitude'],
            clatitude = validated_data['clatitude'],
            cdescription = validated_data['cdescription'],
            cipUser = validated_data['cipUser'],
            nidGender = validated_data['nidGender'],
            nidCity = validated_data['nidCity'],
        )

        #user = models.User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'id': user.pk,
                'password': user.password,
                'cnickname': user.cnickname,
                'cfirstname': user.cfirstname,
                'clastname': user.clastname,
                'dbirthdate': user.dbirthdate,
                'cmail': user.cmail,
                'cavatar_url': user.cavatar.url,
                'cavatar_path': user.cavatar.path,
                'cavatar_b64': b64encode(user.cavatar.read()),
                'cphone': user.cphone,
                'clongitude': user.clongitude,
                'clatitude': user.clatitude,
                'cdescription': user.cdescription,
                'cipUser': user.cipUser,
                'nidGender': user.nidGender.pk,
                'nidCity': user.nidCity.pk,
                })
        except Exception as e:
            return Response({'Error' : 'usuario o contraseña invalidas'}, status=status.HTTP_400_BAD_REQUEST)


class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model= models.Country
        fields='__all__'

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model= models.City
        fields='__all__'

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model= models.Game
        fields='__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model= models.Category
        fields='__all__'

class characteristic_userSerializer(serializers.ModelSerializer):

    class Meta:
        model= models.characteristic_user
        fields='__all__'

class GenderSerializer(serializers.ModelSerializer):

    class Meta:
        model= models.Gender
        fields='__all__'


class Detail_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.detail_user
        fields='__all__'

    def create(self, validated_data):
            detail = models.detail_user.objects.create(**validated_data)
            return detail
        
class Detail_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= models.detail_category
        fields='__all__'

    def create(self, validated_data):
            detail = models.detail_category.objects.create(**validated_data)
            return detail


class Detail_GameSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.detail_game
        fields='__all__'

    def create(self, validated_data):
            detail = models.detail_game.objects.create(**validated_data)
            return detail