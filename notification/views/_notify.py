from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from notification.serializers import NotificationSerializer
from telegram.management.commands.send_telegram_message import Command
from template.formater import TemplateFormater


class NotifyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = NotificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        template_tag = serializer.validated_data["template_tag"]
        template_variables = serializer.validated_data["template_variables"]
        chat_id = serializer.validated_data["chat_id"]
        bot_uuid = serializer.validated_data["bot_uuid"]

        template_formater = TemplateFormater(template_tag)
        text = template_formater.format(template_variables)

        command = Command()
        command.handle(
            text=text,
            chat_id=chat_id,
            bot_uuid=bot_uuid,
        )
        return Response(status=status.HTTP_200_OK)
