from django.contrib import admin
from django.urls import path


from CarService.views import (
    MainView,
    AboutView,
    ServicesView,
    VisitFormView,
    ThanksTemplateView,
    ServicesBySectionView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('appointment/', VisitFormView.as_view(), name='appointment'),
    path('thanks/', ThanksTemplateView.as_view(), name='thanks'),

    # Маршрут для скрипта
    path("get_services_by_section/<int:section_id>/", ServicesBySectionView.as_view(), name="get_services_by_section"),
]
