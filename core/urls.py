
from django.contrib import admin
from django.urls import path, include

from . import views as homeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView.home, name='home'),

    path('portfolio/', include('apps.portfolio.urls'), name='portafolio')
]
