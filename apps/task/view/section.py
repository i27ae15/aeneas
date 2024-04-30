from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from task.models.section import Section
from task.serializers.section import SectionSerializer


class SectionAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            try:
                instance = Section.objects.get(pk=pk)
                serializer = SectionSerializer(instance)
                return Response(serializer.data)
            except Section.DoesNotExist:
                return Response(
                    {"error": "Object does not exist"},
                    status=status.HTTP_404_NOT_FOUND
                    )
        else:
            queryset = Section.objects.all()
            serializer = SectionSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = Section.objects.get(pk=pk)
        except Section.DoesNotExist:
            return Response(
                {"error": "Object does not exist"},
                status=status.HTTP_404_NOT_FOUND
                )

        serializer = SectionSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
