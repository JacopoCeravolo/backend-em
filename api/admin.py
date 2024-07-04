from django.contrib import admin
from .models import Startup, Investor

# Register the model with the admin site
admin.site.register(Startup)
admin.site.register(Investor)