from rest_framework import serializers


class PreparedNotificationSerializer(serializers.Serializer):
    blank_tag = serializers.CharField(max_length=64)
    template_variables = serializers.DictField(required=False, default={})
