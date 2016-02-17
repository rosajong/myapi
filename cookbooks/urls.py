from django.conf.urls import url
from .views import CookbookViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'cookbooks', CookbookViewSet)
urlpatterns = router.urls

# urlpatterns += [url(r'^/?$', home, name='home')]
