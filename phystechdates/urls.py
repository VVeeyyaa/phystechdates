from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('user_profile.urls')),
    path('', include('main.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
