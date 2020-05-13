from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PcSerializer
from .models import Pc

class PcList(APIView):
    def get(self, request, format=None):
        pcs = Pc.objects.all()
        serializer = PcSerializer(pcs, many=True)
        return Response(serializer.data)


class PcDetail(APIView):
    def get_object(self, pk):
        try:
            return Pc.objects.get(pk=pk)
        except Pc.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pc = self.get_object(pk)
        serializer = PcSerializer(pc)
        return Response(serializer.data)


