"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Импортируем модуль администратора Django для управления моделью через веб-интерфейс
from django.urls import path, include  # Импортируем функции для работы с URL-путями

# Список маршрутов URL для проекта
urlpatterns = [
    path('admin/', admin.site.urls),  # URL для доступа к административной панели Django
    path('', include('app.urls')),  # Включаем URL-страницы из приложения 'app' в корень сайта
]