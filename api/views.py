# from django.shortcuts import render
# from django.contrib.auth.models import User
# from rest_framework import generics
# from .serializers import UserSerializer, AccomplishmentSerializer
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from .models import Accomplishment

# # Create your views here.
# class AccomplishmentListCreate(generics.ListCreateAPIView):
#   queryset = Accomplishment.objects.all()
#   serializer_class = AccomplishmentSerializer
#   permission_classes = [IsAuthenticated]

#   def get_queryset(self):
#     user = self.request.user
#     return Accomplishment.objects.filter(user=user)

#   def perform_create(self, serializer):
#     if serializer.is_valid():
#       serializer.save(user=self.request.user)
#     else:
#       print(serializer.errors)

# class AccomplishmentDelete(generics.DestroyAPIView):
#   queryset = Accomplishment.objects.all()
#   serializer_class = AccomplishmentSerializer
#   permission_classes = [IsAuthenticated]

#   def get_queryset(self):
#     user = self.request.user
#     return Accomplishment.objects.filter(user=user)

# class CreateUserView(generics.CreateAPIView):
#   queryset = User.objects.all()
#   permission_classes = [AllowAny]
#   serializer_class = UserSerializer

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, AccomplishmentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Accomplishment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
      print("API root function called")
    return Response({
        'user-registration': reverse('register', request=request, format=format),
        'token': reverse('get_token', request=request, format=format),
        'token-refresh': reverse('refresh_token', request=request, format=format),
        'accomplishments': reverse('accomplishments-list', request=request, format=format),
    })

class AccomplishmentListView(generics.ListCreateAPIView):
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

class AccomplishmentDeleteView(generics.DestroyAPIView):
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