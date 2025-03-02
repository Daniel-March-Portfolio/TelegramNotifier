from rest_framework import serializers


class NotificationSerializer(serializers.Serializer):
    template_tag = serializers.CharField(max_length=64)
    template_variables = serializers.DictField(required=False, default={})
    bot_uuid = serializers.UUIDField()
    chat_id = serializers.IntegerField()
