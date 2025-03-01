from django.contrib import admin

from template.models import Template


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    search_fields = ('tag',)
    readonly_fields = ('uuid', 'created_at', 'updated_at')
