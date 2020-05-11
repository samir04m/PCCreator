from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]