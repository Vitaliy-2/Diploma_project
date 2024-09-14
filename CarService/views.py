from django.shortcuts import render

from django.views.generic import (
    TemplateView,
)


MENU = [
        {'title': 'Главная', 'url': '/', 'alias': 'main'},
        {'title': 'О сервисе', 'url': '#masters', 'alias': 'about'},
        {'title': 'Услуги', 'url': '#services', 'alias': True},
        {'title': 'Отзывы', 'url': '#reviews', 'alias': True},
        {'title': 'Запись', 'url': '#orderForm', 'alias': True},
    ]


def get_menu_context(menu: list[dict] = MENU):
    return {"menu": menu}


class MainView(TemplateView):
    template_name = "main.html"

    # Расширяем метод. Добавляем контекст ключ - меню.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_menu_context())
        context.update({'page_alias': 'main'})
        return context
