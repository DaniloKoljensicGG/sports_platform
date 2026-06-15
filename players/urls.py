from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register("player_profile", views.PlayerProfileViewSet)
router.register("sports", views.SportViewSet)

urlpatterns = router.urls
