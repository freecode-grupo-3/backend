from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import CreateUserViewSet, UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register('create', CreateUserViewSet)
router.register('', UserViewSet)

# Static Routes
urlpatterns = [
    # as view
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Dynamic Routes
urlpatterns += router.urls