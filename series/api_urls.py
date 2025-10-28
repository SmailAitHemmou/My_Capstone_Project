from rest_framework.routers import DefaultRouter
from .api_views import SerieViewSet

router = DefaultRouter()
router.register(r'series', SerieViewSet, basename='serie')

urlpatterns = router.urls