from django.contrib import admin
from .models import Links


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    """Работа с админ панелью"""

    list_display = (
        "id",
        "original_url",
        "short_url",
        "date_of_creation",
        "creator",
    )  # поля, которые видны в админке

    list_editable = (
        "original_url",
        "short_url",
        "creator",
    )  # задаёт поля, которые можно редактировать прямо из общей таблицы
    search_fields = (
        "id",
        "original_url",
        "short_url",
        "date_of_creation",
    )  # добавляет поиск по указанным полям
