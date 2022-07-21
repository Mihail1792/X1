from django.contrib.auth.models import User
from django.db import models


class Links(models.Model):
    original_url = models.URLField("Оригинальная ссылка")
    short_url = models.CharField(
        "Короткая ссылка", max_length=250, unique=True, blank=True
    )
    date_of_creation = models.DateTimeField(
        "Дата создания", auto_now_add=True, blank=True
    )
    creator = models.ForeignKey(
        User,
        verbose_name="Создатель ссылки",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.original_url

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
