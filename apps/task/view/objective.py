from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from task.models.objetives import Objective
from django.shortcuts import get_object_or_404
from task.models.section import Section
from task.serializers.objective import ObjectiveSerializer


class ObjectiveAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, section_pk=None, objective_pk=None):
        if section_pk and objective_pk:
            try:
                instance = Objective.objects.get(
                    pk=objective_pk,
                    section__user=request.user,
                    section__pk=section_pk
                    )
                serializer = ObjectiveSerializer(instance)
                return Response(serializer.data)
            except Objective.DoesNotExist:
                return Response(
                    {"error": "Object does not exist"},
                    status=status.HTTP_404_NOT_FOUND
                            )
        else:
            queryset = Objective.objects.filter(
                section__user=request.user
            )
            serializer = ObjectiveSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request, section_pk=None):
        section = get_object_or_404(Section, pk=section_pk)
        serializer = ObjectiveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(section=section)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, section_pk=None, objective_pk=None):
        try:
            instance = Objective.objects.get(
                pk=objective_pk,
                section__pk=section_pk,
                section__user=request.user
                )
        except Objective.DoesNotExist:
            return Response(
                {'error': 'Object does not exist'},
                status=status.HTTP_404_NOT_FOUND)

        serializer = ObjectiveSerializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, section_pk=None, objective_pk=None):
        try:
            instance = Objective.objects.get(
                pk=objective_pk,
                section__pk=section_pk,
                section__user=request.user
                )
        except Objective.DoesNotExist:
            return Response(
                {"error": "Object does not exist"},
                status=status.HTTP_404_NOT_FOUND
                )

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
