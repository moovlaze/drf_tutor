from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer

class WomenAPIView(APIView):
    def get(self, request):
        serialize = WomenSerializer(Women.objects.all())
        print(serialize.data)
        return Response({'Post': 'this is my post'})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
