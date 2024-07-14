from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Accomplishment

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'password', 'id']
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user

class AccomplishmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Accomplishment
    fields = '__all__'
    extra_kwargs = {'user': {'read_only': True}}