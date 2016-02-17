from django.conf.urls import url
from .views import RecipeViewSet, home
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'recipes', RecipeViewSet)
urlpatterns = router.urls

urlpatterns += [url(r'^/?$', home, name='home')]
