from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('coaching.urls')),
    path('admin/', admin.site.urls),
]
