from django.contrib.auth.models import User
from django.db import models


class Links(models.Model):
    original_url = models.URLField('Оригинальная ссылка')
    short_url = models.CharField('Короткая ссылка', max_length=250, unique=True, blank=True)
    # unique=True (уникальное поле), blank=True (может быть пустым, если не указываем, то по дефолту False)
    date_of_creation = models.DateTimeField('Дата создания', auto_now_add=True, blank=True)
    creator = models.ForeignKey(User, verbose_name='Создатель ссылки', on_delete=models.CASCADE, null=True, blank=True)
    # null=True если автор не указан, то в базе будет null
    # так же существует параметр default, к примеру default=1 будет устанавливать id=1
    # https://stackoverflow.com/questions/16589069/foreignkey-does-not-allow-null-values если поле---->
    # с ForeignKey создавалось после создания модели, то для корректной работы нужно установить null=True, blank=True

    def __str__(self):
        return self.original_url

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'