from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, single_product, works

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('project/', single_product),
    path('works/', works)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)