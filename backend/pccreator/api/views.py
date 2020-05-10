from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PcSerializer
from .models import *

class PcViewSet(viewsets.ModelViewSet):
    queryset = Pc.objects.all()
    serializer_class = PcSerializer
    permission_classes = [permissions.IsAuthenticated]
