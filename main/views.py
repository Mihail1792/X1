from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.generic import ListView
from main.models import Links
from main.utils import create_random_code


def index(request):
    """Представление основной страницы"""

    data = {}
    shot = create_random_code()  # генерирует короткую часть
    current_user = get_user(request)  # объект текущего пользователя
    current_user_is_auth = (
        current_user.is_authenticated
    )  # указывает аутентифицирован ли пользователь

    if request.method == "POST":
        user_url = request.POST.get("link")  # получает данные из формы

        if current_user_is_auth:  # если пользователь аутентифицирован

            if Links.objects.filter(
                creator=current_user, original_url=user_url
            ).exists():  # проверяет, есть ли
                # такая ссылка в бд
                # если есть
                get_model_short_url = (
                    Links.objects.get(original_url=user_url, creator=current_user)
                ).short_url
                give_to_user_short_url = (
                    request.build_absolute_uri("/") + get_model_short_url
                )  # строит короткую ссылку
                data["give_to_user_short_url"] = give_to_user_short_url

                return render(request, "main/index.html", data)
                # отдаём пользователю короткую ссылку, не перезаписывая данные в бд

            else:
                # иначе
                Links(
                    creator=current_user, original_url=user_url, short_url=shot
                ).save()  # сохраняем в бд
                give_to_user_short_url = (
                    request.build_absolute_uri("/") + shot
                )  # формируем короткий юрл
                data[
                    "give_to_user_short_url"
                ] = give_to_user_short_url  # добавляем в словарь

                return render(
                    request, "main/index.html", data
                )  # отдаём шаблон с коротким url
        else:
            # если пользователь не аутентифицирован
            Links(original_url=user_url, short_url=shot).save()
            give_to_user_short_url = request.build_absolute_uri("/") + shot
            data["give_to_user_short_url"] = give_to_user_short_url
            return render(request, "main/index.html", data)
    else:
        return render(request, "main/index.html")  # если метод GET, отдаём шаблон


def redirect_original_url(request, shortened_part):
    """Перенаправляет с укороченной ссылки на оригинальную"""

    try:
        shortener = Links.objects.get(short_url=shortened_part)
        return HttpResponseRedirect(shortener.original_url)
    except:
        raise Http404("Извините, эта ссылка не работает :(")


class ProfileView(LoginRequiredMixin, ListView):
    """Представление кабинета пользователя"""

    model = Links
    template_name = "main/profile.html"
    context_object_name = "auth_user_links"

    def get_queryset(self):
        return Links.objects.filter(creator=self.request.user).order_by(
            "-date_of_creation"
        )
