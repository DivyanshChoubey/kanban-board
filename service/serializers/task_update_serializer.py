from rest_framework import serializers


class TaskUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    time = serializers.IntegerField(required=False)
    end_time = serializers.DateTimeField(required=False)
    status = serializers.CharField(required=False)
