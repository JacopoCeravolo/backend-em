from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/', include('api.urls')),
    path('matcher/', include('matcher.urls')),
    path('accounts/', include('allauth.urls')),  # This line includes allauth URLs
]
