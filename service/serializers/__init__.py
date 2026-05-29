__all__=[
    "UserSerializer",
    "TaskUrlSerializer",
    "TasksSerializer",
    "TaskCreateSerializer",
    "TaskGetSerializer",
    "TaskUpdateSerializer",
]

from service.serializers.user_serializer import UserSerializer
from service.serializers.task_url_serializer import TaskUrlSerializer
from service.serializers.task_create_serializer import TaskCreateSerializer
from service.serializers.task_get_serializer import TaskGetSerializer
from service.serializers.task_update_serializer import TaskUpdateSerializer
