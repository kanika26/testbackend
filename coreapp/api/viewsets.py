from rest_framework.viewsets import ModelViewSet
from coreapp.models import User, Category, SubCategory, Product, SendGridIntegration
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import (
    UserSerializer,
    UserInfoSerializer,
    CategorySerializer,
    SubCategorySerializer,
    ProductSerializer,
    SendGridIntegrationSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    @action(detail=False, methods=["get"])
    def info(self, request):
        user = request.user
        userinfoserializer = UserInfoSerializer(user)
        return Response(userinfoserializer.data)

    @action(detail=False, methods=["post"])
    def change_password(self, request):
        user = request.user
        data = request.data
        user.change_password(data["new_password"])
        return Response(status=204)

    @action(detail=False, methods=["post"])
    def change_email(self, request):
        user = request.user
        data = request.data
        user.change_email(data["new_email"])
        return Response(status=204)


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SubCategoryViewSet(ModelViewSet):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        return SubCategory.objects.filter(category__user=self.request.user)


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(subcategory__category__user=self.request.user)


class SendGridIntegrationViewSet(ModelViewSet):
    queryset = SendGridIntegration.objects.all()
    serializer_class = SendGridIntegrationSerializer
