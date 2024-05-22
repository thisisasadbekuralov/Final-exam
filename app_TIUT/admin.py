from django.contrib import admin
from .models import Requirements, FAQ, Review, Sphere, Paper, Publication


class PaperAdmin(admin.ModelAdmin):
    exclude = ('views_count',)


class PublicationAdmin(admin.ModelAdmin):
    exclude = ('views_count',)


admin.site.register(FAQ)
admin.site.register(Requirements)
admin.site.register(Review)
admin.site.register(Sphere)
admin.site.register(Paper, PaperAdmin)
admin.site.register(Publication, PublicationAdmin)