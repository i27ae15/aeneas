from rest_framework import serializers
from apps.task.models import section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = section
        fields = '__all__'
