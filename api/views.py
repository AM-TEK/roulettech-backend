from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, AccomplishmentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Accomplishment

# Create your views here.
class AccomplishmentListCreate(generics.ListCreateAPIView):
  queryset = Accomplishment.objects.all()
  serializer_class = AccomplishmentSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    user = self.request.user
    return Accomplishment.objects.filter(user=user)

  def perform_create(self, serializer):
    if serializer.is_valid():
      serializer.save(user=self.request.user)
    else:
      print(serializer.errors)

class AccomplishmentDelete(generics.DestroyAPIView):
  queryset = Accomplishment.objects.all()
  serializer_class = AccomplishmentSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    user = self.request.user
    return Accomplishment.objects.filter(user=user)

class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  permission_classes = [AllowAny]
  serializer_class = UserSerializer