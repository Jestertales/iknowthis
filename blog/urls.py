from rest_framework.routers import DefaultRouter
from blog import views

router = DefaultRouter()
router.register(r'posts', views.BlogViewSet, basename='blog')

urlpatterns = router.urls

