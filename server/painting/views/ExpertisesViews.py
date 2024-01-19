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
def get_expertises(request):
    exps = Expertises.objects.all()
    serializer = ExpertiseSerializer(exps, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def get_expertise_by_id(request, e_id):
    if not Expertises.objects.filter(pk=e_id).exists():
        return Response(f"Экспертизы с таким id не существует!")

    expertise = Expertises.objects.get(pk=e_id)
    serializer = ExpertiseSerializer(expertise, many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def update_expertise(request, e_id):
    if not Expertises.objects.filter(pk=e_id).exists():
        return Response(f"Экспертизы с таким id не существует!")

    expertise = Expertises.objects.get(pk=e_id)
    serializer = ExpertiseSerializer(expertise, data=request.data, many=False, partial=True)

    if serializer.is_valid():
        serializer.save()

    expertise.status = 1
    expertise.save()

    return Response(serializer.data)

@api_view(["PUT"])
def update_expertise_user(request, e_id):
    if not Expertises.objects.filter(pk=e_id).exists():
        return Response(f"Экспертизы с таким id не существует!")

    e_status = request.data["status"]

    if e_status not in [1, 5]:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    exp = Expertises.objects.get(pk=e_id)
    status = exp.status

    if status == 5:
        return Response("Статус изменить нельзя")

    exp.status = e_status
    exp.save()

    serializer = ExpertiseSerializer(exp, many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def update_expertise_admin(request, e_id):
    if not Expertises.objects.filter(pk=e_id).exists():
        return Response(f"Экспертизы с таким id не существует!")

    e_status = request.data["status"]

    if e_status in [1, 5]:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    exp = Expertises.objects.get(pk=e_id)

    status = exp.status

    if status in [3, 4, 5]:
        return Response("Статус изменить нельзя")

    exp.status = e_status
    exp.save()

    serializer = ExpertiseSerializer(exp, many=False)
    return Response(serializer.data)

@api_view(["DELETE"])
def delete_expertise(request, e_id):

    if not Expertises.objects.filter(pk=e_id).exists():
        return Response(f"Экспертизы с таким id не существует!")

    exp = Expertises.objects.get(pk=e_id)
    exp.status = 5
    exp.save()
    serializer = ExpertiseSerializer(exp, many=True)
    return Response(serializer.data)

@api_view(["DELETE"])
def delete_painting_from_expertise(request, e_id, p_id):
    if not Expertises.objects.filter(pk=e_id).exists():
        return Response(f"Экспертизы с таким id не существует")

    if not  Paintings.objects.filter(pk=p_id).exists():
        return Response(f"Картины с таким id не существует")

    exp = Expertises.objects.get(pk=e_id)
    exp.paintings.remove(Paintings.objects.get(pk=p_id))
    exp.save()

    serializer = ExpertiseSerializer(exp.paintings, many=True)
    return Response(serializer.data)