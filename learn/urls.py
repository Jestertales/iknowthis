from rest_framework.routers import DefaultRouter
from .views import LearningResourceViewSet, TopicViewSet

router = DefaultRouter()
router.register(r'learning-resources', LearningResourceViewSet)
router.register(r'topics', TopicViewSet)

urlpatterns = router.urls
