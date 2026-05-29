from rest_framework import serializers
from service.serializers.task_url_serializer import TaskUrlSerializer
from service.models import Tasks

class TaskGetSerializer(serializers.ModelSerializer):
    urls = TaskUrlSerializer(many=True, read_only=True)
    class Meta:
        model = Tasks
        fields = [
            "id",
            "title",
            "description",
            "time",
            "start_time",
            "end_time",
            "status",
            "parent_task",
            "urls",
        ]
