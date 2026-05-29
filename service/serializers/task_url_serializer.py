from rest_framework import serializers


class TaskUrlSerializer(serializers.Serializer):
    url = serializers.URLField()
    url_type = serializers.CharField(max_length=30)
