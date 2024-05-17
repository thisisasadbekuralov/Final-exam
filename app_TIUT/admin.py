from django.contrib import admin

# Register your models here.

from .models import Requirements, FAQ

admin.site.register(FAQ)
admin.site.register(Requirements)