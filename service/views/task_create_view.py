from rest_framework.views import APIView
from service.serializers import TaskCreateSerializer
from rest_framework.response import Response
from service.constants import ResponseMessages
from rest_framework import status
from service.models import User, Tasks, TaskURL



class TaskCreateView(APIView):
    def post(self, request):
        serializer = TaskCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "success":False,
                    "message":ResponseMessages.INVALID_DATA,
                    "error":serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        data = serializer.validated_data
        try:
            user = User.objects.get(id=data["user"])
        except User.DoesNotExist:
            return  Response(
                {
                    "success": False,
                    "message": ResponseMessages.NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )
        parent_task = None
        if data.get("parent_task"):
            try:
                parent_task = Tasks.objects.get(id=data["parent_task"])
            except Tasks.DoesNotExist:
                return Response(
            {
                "success": False,
                "message": ResponseMessages.PARENT_NOT_FOUND
            },
            status=status.HTTP_404_NOT_FOUND
        )
        task = Tasks.objects.create(
            user=user,
            title=data["title"],
            description=data.get("description"),
            time=data.get("time"),
            start_time=data.get("start_time"),
            end_time=data.get("end_time"),
            status=data.get("status"),
            parent_task=parent_task
        )
        url = data.get("urls",[])
        for url_data in url:
            TaskURL.objects.create(
                task=task,
                url=url_data["url"],
                url_type=url_data["url_type"]
            )

        return Response(
            {
                "success":True,
                "message":ResponseMessages.TASK_CREATE
            },
            status=status.HTTP_200_OK
        )
