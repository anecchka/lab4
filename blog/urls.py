from django.contrib import admin
from django.urls import path, include  # Добавляем include в импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')),  # Убедитесь, что нет лишних пробелов
]