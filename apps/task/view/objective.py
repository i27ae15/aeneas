from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from task.models.objetives import Objective
from task.serializers.objective import ObjectiveSerializer


class ObjectiveAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            try:
                instance = Objective.objects.get(
                    pk=pk,
                    section__user=request.user
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

#     def post(self, request):
#         serializer = ObjectiveSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def put(self, request, pk):
#         try:
#             instace = Objective.objects.get(pk=pk, data=request.data)
#         except Objective.DoesNotExist:
#             return Response(
#                 {'error': 'Object does not exist'},
#                 status=status.HTTP_400_BAD_REQUEST)

#         serializer = ObjectiveSerializer(instace, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         try:
#             instance = Objective.objects.get(pk=pk, user=Response.user)
#         except Objective.DoesNotExist:
#             return Response(
#                 {"error": "Object does not exist"},
#                 status=status.HTTP_404_NOT_FOUND
#                 )

#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
