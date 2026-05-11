from rest_framework import serializers

class SystemStatusSerializer(serializers.Serializer):
    status = serializers.CharField()
    version = serializers.CharField()
    uptime = serializers.CharField()
    cpu_usage = serializers.FloatField()
    ram_usage = serializers.FloatField()
