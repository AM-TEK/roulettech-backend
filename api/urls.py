# from django.urls import path
# from . import views

# urlpatterns = [
#   path('accomplishments/', views.AccomplishmentListCreate.as_view(), name='accomplishments-list'),
#   path('accomplishments/delete/<int:pk>/', views.AccomplishmentDelete.as_view(), name='accomplishment-delete'),
# ]

from django.urls import path
from .views import AccomplishmentListView, AccomplishmentDeleteView
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Test view working")

urlpatterns = [
    path('accomplishments/', AccomplishmentListView.as_view(), name='accomplishments-list'),
    path('accomplishments/delete/<int:pk>/', AccomplishmentDeleteView.as_view(), name='accomplishment-delete'),
    path('', test_view, name='test'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]