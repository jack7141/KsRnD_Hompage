from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from product.views import index, single_product, works

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('project/<id>/', single_product, name='single_product'),
    path('works/<id>/', works, name='works')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)