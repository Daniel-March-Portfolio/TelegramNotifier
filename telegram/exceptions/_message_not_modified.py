class TelegramMessageNotModifiedException(Exception):
    def __init__(self):
        super().__init__('Message not modified')
