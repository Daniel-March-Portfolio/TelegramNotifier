from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView

from blank.models import Blank
from blank.serializers import SendBlankSerializer
from telegram.management.commands.send_telegram_message import Command
from template.formater import TemplateFormater


class SendAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SendBlankSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blank_tag = serializer.validated_data["blank_tag"]
        template_variables = serializer.validated_data["template_variables"]

        blank = get_object_or_404(Blank, tag=blank_tag)
        variables = blank.template_variables
        template_formater = TemplateFormater(blank.template.tag)
        variables.update(template_variables)
        text = template_formater.format(variables)

        command = Command()
        message_id = command.handle(
            text=text,
            chat_id=blank.chat_id,
            bot_uuid=blank.bot.uuid,
        )
        return JsonResponse(
            data={
                'message_id': message_id,
            },
            status=status.HTTP_200_OK
        )
