class TelegramUserDeactivatedException(Exception):
    def __init__(self):
        super().__init__('Telegram user is deactivated')
