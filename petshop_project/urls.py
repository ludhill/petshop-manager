# petshop_project/urls.py
from django.contrib import admin
from django.urls import path, include
from management.views import home
from django.conf import settings             # <-- IMPORTE settings
from django.conf.urls.static import static # <-- IMPORTE static

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls), # <-- LUGAR CORRETO PARA ESTA LINHA
    path('management/', include('management.urls')),
]

# Adiciona as URLs de mídia apenas em modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)