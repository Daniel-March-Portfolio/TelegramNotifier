from django.contrib import admin

from blank.models import Blank, BlankVariable


class BlankVariableInline(admin.TabularInline):
    model = BlankVariable
    fields = ('type', 'key', '_value',)
    extra = 0


@admin.register(Blank)
class BlankAdmin(admin.ModelAdmin):
    inlines = [BlankVariableInline]
    list_display = ('tag', 'bot', 'chat_id',)
    search_fields = ('tag', 'bot__name', '_chat_id',)
    list_filter = ('bot', '_chat_id',)
    readonly_fields = ('uuid',)
