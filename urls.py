from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Test view working")

urlpatterns = [
    path('', test_view, name='test'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]