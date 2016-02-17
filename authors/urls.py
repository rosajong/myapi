from rest_framework.routers import SimpleRouter
from .views import AuthorViewSet

router = SimpleRouter()
router.register(r'authors', AuthorViewSet)
urlpatterns = router.urls
