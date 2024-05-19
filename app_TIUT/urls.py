from django.urls import path
from rest_framework import routers

from .views import FAQViewSet, RequirementsViewSet, send_email


router = routers.DefaultRouter()
router.register('faqs', FAQViewSet)
router.register('requirements', RequirementsViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('send-email/', send_email),
]