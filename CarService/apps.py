from django.apps import AppConfig


class CarserviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CarService'
    verbose_name = 'Записи клиентов'

    # По готовности приложения будет импортирован сигнал
    def ready(self):
        import CarService.signals
