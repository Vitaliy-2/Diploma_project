from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    FormView,
)
from .forms import VisitModelForm



MENU = [
        {'title': 'Главная', 'url': '/', 'alias': 'main'},
        {'title': 'О сервисе', 'url': '/about/', 'alias': 'about'},
        {'title': 'Услуги', 'url': '/services/', 'alias': 'services'},
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


class AboutView(TemplateView):
    template_name = "about.html"

    # Расширяем метод. Добавляем контекст ключ - меню.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_menu_context())
        context.update({'page_alias': 'about'})
        return context


class ServicesView(TemplateView):
    template_name = "services.html"

    # Расширяем метод. Добавляем контекст ключ - меню.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_menu_context())
        context.update({'page_alias': 'services'})
        return context


# класс для отображения форм
class VisitFormView(FormView):
    template_name = "visit_form.html"
    form_class = VisitModelForm
    success_url = "/thanks/"
    context = get_menu_context()

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# Используется для статичных страниц, где данные особо не меняются
class ThanksTemplateView(TemplateView):
    template_name = "thanks.html"
    
    # Расширяем метод. Добавляем контекст ключ - меню.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_menu_context())
        return context
