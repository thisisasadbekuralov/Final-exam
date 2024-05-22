from django.urls import path
from rest_framework import routers

from .views import (FAQViewSet,
                    RequirementsViewSet,
                    send_email,
                    SphereViewSet,
                    PublicationViewSet,
                    PaperViewSet,
                    ReviewViewSet,
                    main_page_details,
                    paper_detail_with_reviews,
                    UserInfoList,
                    )


router = routers.DefaultRouter()
router.register('faqs', FAQViewSet)
router.register('requirements', RequirementsViewSet)
router.register('sphere', SphereViewSet)
router.register('publications', PublicationViewSet)
router.register('papers', PaperViewSet)
router.register('reviews', ReviewViewSet)
# router.register('userinfo', UserInfoList)


urlpatterns = router.urls

urlpatterns += [
    path('send-email/', send_email),
    path('main-page-details/', main_page_details),
    path('paper-detail-with-reviews/<int:id>', paper_detail_with_reviews),
    path('user-info-list/', UserInfoList.as_view()),
]