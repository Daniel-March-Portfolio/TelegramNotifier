from django.contrib import admin

from telegram.models import TelegramBot


@admin.register(TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):
    list_display = ("name", "token", "uuid")
    search_fields = ("name", "token")

    readonly_fields = ("uuid",)