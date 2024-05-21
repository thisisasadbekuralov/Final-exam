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
router.register('publications', PublicationViewSet) #need to add filters
router.register('papers', PaperViewSet) #need to do filter
router.register('reviews', ReviewViewSet) #need to add reviews
# router.register('userinfo', UserInfoList)


urlpatterns = router.urls

urlpatterns += [
    path('send-email/', send_email),
    path('main-page-details/', main_page_details),
    path('paper-detail-with-reviews/<int:paper_id>', paper_detail_with_reviews), #need to check mistakes
    path('user-info-list/', UserInfoList.as_view()),
]