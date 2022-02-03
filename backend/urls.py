from rest_framework.routers import DefaultRouter

from .views import ReferenceViewSet

router = DefaultRouter()

router.register('', ReferenceViewSet)

urlpatterns = [
]

# Dynamic Routes
urlpatterns += router.urls