from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    email = serializers.EmailField()
