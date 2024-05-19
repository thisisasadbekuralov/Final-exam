from django.contrib import admin

# Register your models here.

from .models import Requirements, FAQ, Review, Sphere, Paper, Publication

admin.site.register(FAQ)
admin.site.register(Requirements)
admin.site.register(Review)
admin.site.register(Sphere)
admin.site.register(Paper)
admin.site.register(Publication)

