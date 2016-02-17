from django.conf.urls import url

from .views import IngredientViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'ingredients', IngredientViewSet)
urlpatterns = router.urls
