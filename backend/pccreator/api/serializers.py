from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class PcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pc
        fields = ['id', 'name', 'budget', 'create_at']