from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from task.models.task import Task
from task.models.objetives import Objective
from task.models.section import Section
from task.serializers.task import TaskSerializer
from django.shortcuts import get_object_or_404


class TaskeAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, section_pk=None, objective_pk=None, task_pk=None):
        if section_pk and objective_pk and task_pk:
            try:
                instance = Task.objects.get(
                    pk=task_pk,
                    objective__section__user=request.user,
                    objective__section__pk=section_pk,
                    objective__pk=objective_pk
                    )
                serializer = TaskSerializer(instance)
                return Response(serializer.data)
            except Task.DoesNotExist:
                return Response(
                    {"error": "Object does not exist"},
                    status=status.HTTP_404_NOT_FOUND
                            )
        else:
            queryset = Task.objects.filter(
                 objective__section__user=request.user,
                 objective__section__pk=section_pk
                )
            serializer = TaskSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request, section_pk=None, objective_pk=None):
        section = get_object_or_404(Section, pk=section_pk)
        objective = get_object_or_404(
            Objective, pk=objective_pk,
            section=section
            )
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(objective=objective)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, section_pk=None, objective_pk=None, task_pk=None):
        try:
            instance = Task.objects.get(
                pk=task_pk,
                objective__section__user=request.user,
                objective__section__pk=section_pk,
                objective__pk=objective_pk
            )
        except Task.DoesNotExist:
            return Response(
                {'error': 'Object does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TaskSerializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, section_pk=None, objective_pk=None, task_pk=None):
        try:
            instance = Task.objects.get(
                pk=task_pk,
                objective__section__user=request.user,
                objective__section__pk=section_pk,
                objective__pk=objective_pk
            )
        except Task.DoesNotExist:
            return Response(
                {"error": "Object does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
