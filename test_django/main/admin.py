from django.contrib import admin
from .models import Links


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    """Работа с админ панелью"""

    # https://www.youtube.com/watch?v=SZ-kPr4Z38A
    list_display = (
        "id",
        "original_url",
        "short_url",
        "date_of_creation",
        "creator",
    )  # поля, которые видны в админке
    # list_display_links = ('id', 'original_url', 'short_url', 'date_of_creation', 'creator') # если указано в линкс, то можно прожимать
    # list_filter = ('original_url', 'short_url', 'date_of_creation', 'creator', 'creator__id') # добавляет фильтрацию по указанным полям
    # 'creator__id' добаляет в таблицу фильтрацию по полю id связанной модели
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
