from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'full_name', 'stance')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'full_name', 'stance')

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            full_name = validated_data['full_name'],
            stance = validated_data['stance']
        )

        user.save()

        return user


