from rest_framework import serializers


class UpdateBlankSerializer(serializers.Serializer):
    message_id = serializers.IntegerField()
    blank_tag = serializers.CharField(max_length=64)
    template_variables = serializers.DictField(required=False, default={})
