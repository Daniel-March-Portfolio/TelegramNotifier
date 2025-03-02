class TelegramBotNotFoundException(Exception):
    def __init__(self):
        super().__init__('Bot not found')
