# from django.urls import path
# from . import views

# urlpatterns = [
#   path('accomplishments/', views.AccomplishmentListCreate.as_view(), name='accomplishments-list'),
#   path('accomplishments/delete/<int:pk>/', views.AccomplishmentDelete.as_view(), name='accomplishment-delete'),
# ]

from django.urls import path
from .views import AccomplishmentListView, AccomplishmentDeleteView

urlpatterns = [
    path('accomplishments/', AccomplishmentListView.as_view(), name='accomplishments-list'),
    path('accomplishments/delete/<int:pk>/', AccomplishmentDeleteView.as_view(), name='accomplishment-delete'),
]