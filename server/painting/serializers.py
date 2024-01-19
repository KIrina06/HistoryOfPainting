from rest_framework import serializers

from .models import *


class PaintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paintings
        fields = "__all__"

class ExpertiseSerializer(serializers.ModelSerializer):
    paintings = PaintingSerializer(read_only=True, many=True)

    class Meta:
        model = Expertises
        fields = "__all__"
