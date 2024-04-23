from rest_framework import serializers
from apps.task.models import Objective


class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = '__all__'
