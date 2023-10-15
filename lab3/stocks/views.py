from django.forms import model_to_dict
from django.shortcuts import render

from .serializers import ExpertiseSerializer
from .models import Expertise, Status
#from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


class StocksAPIView(APIView):
    def get(self, request):
        lst = Expertise.objects.all().values()
        return Response({'posts': list(lst)})
    
    def post(self, request):
        serializer = ExpertiseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method put is not allowed"})
        
        try:
            instance = Expertise.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exisis"})
        
        serializer = ExpertiseSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        
        try:
            instance = Expertise.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"error": "Object does not exisis"})

        return Response({"post": "delete post " + str(pk)})
    

class StocksAPIView1(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method get is not allowed"})
        
        try:
            instance = Expertise.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exisis"})
        
        serializer = ExpertiseSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        return Response({"post": serializer.data})