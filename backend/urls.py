from rest_framework.routers import DefaultRouter

from .views import DiseaseViewSet, ReferenceTypeViewSet, ReferenceViewSet

router = DefaultRouter()

router.register('references', ReferenceViewSet)
router.register('diseases', DiseaseViewSet)
router.register('reference-types', ReferenceTypeViewSet)

urlpatterns = [
]

# Dynamic Routes
urlpatterns += router.urls