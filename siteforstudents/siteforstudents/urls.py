from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from siteforstudents import settings
from homepage.views import *
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = pageNotFound