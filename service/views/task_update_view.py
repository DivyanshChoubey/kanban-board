from rest_framework.views import APIView
from service.serializers import TaskUpdateSerializer
from rest_framework.response import Response
from service.constants import ResponseMessages
from rest_framework import status
from service.models import Tasks


class TaskUpdateView(APIView):
    def patch(self, request):
        serializer = TaskUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "message": ResponseMessages.INVALID_DATA,
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        data = serializer.validated_data
        try:
            task = Tasks.objects.get(id=data["id"])
        except Tasks.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": ResponseMessages.NOT_FOUND
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if "title" in data:
            task.title = data["title"]
        if "description" in data:
            task.description = data["description"]
        if "time" in data:
            task.time = data["time"]
        if "start_time" in data:
            task.start_time = data["start_time"]
        if "end_time" in data:
            task.end_time = data["end_time"]
        if "status" in data:
            task.status = data["status"]
        task.save()

        return Response(
            {
                "success": True,
                "message": ResponseMessages.TASK_UPDATE
            },
            status=status.HTTP_200_OK
        )
