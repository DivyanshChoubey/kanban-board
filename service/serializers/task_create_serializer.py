from rest_framework import serializers
from service.serializers.task_url_serializer import TaskUrlSerializer


class TaskCreateSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField( required=False, allow_blank=True, allow_null=True)
    time = serializers.IntegerField(required=False)
    start_time = serializers.DateTimeField(required=False)
    end_time = serializers.DateTimeField(required=False)
    status = serializers.CharField(required=False)
    parent_task = serializers.IntegerField(required=False, allow_null=True)
    urls = TaskUrlSerializer(many=True, required=False)
