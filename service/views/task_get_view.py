from  rest_framework.views import APIView
from service.models import Tasks
from service.serializers import TaskGetSerializer
from rest_framework.response import Response
from service.constants import ResponseMessages
from rest_framework import status

class TaskGetView(APIView):
    def get(self, request):
        task = Tasks.objects.all().order_by("-id")
        serializer = TaskGetSerializer(task, many=True)

        return Response(
            {
                "success":True,
                "message":ResponseMessages.TASK_FETCH,
                "data":serializer.data
            },
            status=status.HTTP_200_OK
        )
