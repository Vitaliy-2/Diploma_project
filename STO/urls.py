from django.contrib import admin
from django.urls import path


from CarService.views import (
    MainView,
    AboutView,
    ServicesView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
]
