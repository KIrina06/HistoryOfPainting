import ast
import time

from operator import itemgetter
from django.conf import settings
from django.http import HttpResponse
from django.core.cache import cache
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import *
from ..models import *

@api_view(["GET"])
def get_paintings(request):
    paintings = Paintings.objects.all()
    serializer = PaintingSerializer(paintings, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def get_painting_by_id(request, p_id):
    if not Paintings.objects.filter(pk=p_id).exists():
        return Response(f"Картины с таким id не существует!")

    painting = Paintings.objects.get(pk=p_id)
    serializer = PaintingSerializer(painting, many=False)

    return Response(serializer.data)

@api_view(["POST"])
def create_painting(request):
    Paintings.objects.create()

    paintings = Paintings.objects.all()
    serializer = PaintingSerializer(paintings, many=True)
    return Response(serializer.data)

@api_view(["PUT"])
def update_painting(request, p_id):
    if not Paintings.objects.filter(pk=p_id).exists():
        return Response(f"Картины с таким id не существует!")

    painting = Paintings.objects.get(pk=p_id)
    serializer = PaintingSerializer(painting, data=request.data, many=False, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(["DELETE"])
def delete_painting(request, p_id):
    if not Paintings.objects.filter(pk=p_id).exists():
        return Response(f"Картины с таким id не существует!")

    painting = Paintings.objects.get(pk=p_id)
    painting.status = 2
    painting.save()

    paintings = Paintings.objects.filter(status=1)
    serializer = PaintingSerializer(paintings, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def add_painting_to_expertise(request, p_id):

    if not Paintings.objects.filter(pk=p_id).exists():
        return Response(f"Картины с таким id не существует!")

    painting = Paintings.objects.get(pk=p_id)

    expertise = Expertises.objects.filter(status=1).last()

    if expertise is None:
        expertise = Expertises.objects.create()

    expertise.paintings.add(painting)
    expertise.save()

    serializer = PaintingSerializer(expertise.paintings, many=True)
    return Response(serializer.data)
