from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MonsterViewSet, ItemViewSet, UtilisateurViewSet  # Utilisez .views pour une importation relative

router = DefaultRouter()
router.register(r'monsters', MonsterViewSet)
router.register(r'items', ItemViewSet)
router.register(r'Utilisateurs', UtilisateurViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]