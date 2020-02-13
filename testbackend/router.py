from rest_framework import routers
from coreapp.api.viewsets import (
    UserViewSet,
    CategoryViewSet,
    SubCategoryViewSet,
    ProductViewSet,
    SendGridIntegrationViewSet,
)

router = routers.SimpleRouter()
router.register(r"user", UserViewSet)
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"subcategory", SubCategoryViewSet, basename="subcategory")
router.register(r"product", ProductViewSet, basename="product")
router.register(r"sendgridintegration", SendGridIntegrationViewSet)
