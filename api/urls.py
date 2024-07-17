from django.urls import path
from . import views

urlpatterns = [
  path('accomplishments/', views.AccomplishmentListCreate.as_view(), name='accomplishments-list'),
  path('accomplishments/delete/<int:pk>/', views.AccomplishmentDelete.as_view(), name='accomplishment-delete'),
]