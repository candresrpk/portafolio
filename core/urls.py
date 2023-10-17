
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views as homeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView.home, name='home'),

    path('portfolio/', include('apps.portfolio.urls'), name='portafolio')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
