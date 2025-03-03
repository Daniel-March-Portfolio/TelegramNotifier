import logging
from django.http import JsonResponse
from telegram.exceptions import (
    TelegramChatNotFoundException, TelegramBotNotFoundException,
    TelegramBotBlockedException, TelegramUserDeactivatedException,
    TelegramBadMessageException, TelegramMessageNotFoundException,
    TelegramMessageNotModifiedException
)

logger = logging.getLogger(__name__)

class CastExceptionsToResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, _, exception):
        if isinstance(exception, TelegramChatNotFoundException):
            return JsonResponse({'error': 'Chat not found'}, status=404)
        if isinstance(exception, TelegramBotNotFoundException):
            return JsonResponse({'error': 'Bot not found'}, status=404)
        if isinstance(exception, TelegramBotBlockedException):
            return JsonResponse({'error': 'Bot blocked'}, status=403)
        if isinstance(exception, TelegramUserDeactivatedException):
            return JsonResponse({'error': 'User deactivated'}, status=403)
        if isinstance(exception, TelegramBadMessageException):
            return JsonResponse({'error': 'Bad message'}, status=400)
        if isinstance(exception, TelegramMessageNotFoundException):
            return JsonResponse({'error': 'Message not found'}, status=404)
        if isinstance(exception, TelegramMessageNotModifiedException):
            return JsonResponse({'error': 'Message not modified'}, status=400)
        logger.exception(exception)
        return JsonResponse({'error': 'Internal server error'}, status=500)