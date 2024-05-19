from django.urls import path
from rest_framework import routers

from .views import (FAQViewSet,
                    RequirementsViewSet,
                    send_email,
                    SphereViewSet,
                    PublicationViewSet,
                    PaperViewSet,
                    ReviewViewSet
                    )


router = routers.DefaultRouter()
router.register('faqs', FAQViewSet)
router.register('requirements', RequirementsViewSet)
router.register('sphere', SphereViewSet)
router.register('publications', PublicationViewSet)
router.register('papers', PaperViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('send-email/', send_email),
]