class TelegramBotBlockedException(Exception):
    def __init__(self):
        super().__init__('Bot blocked')
