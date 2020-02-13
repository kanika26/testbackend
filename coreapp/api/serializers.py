from rest_framework.serializers import ModelSerializer
from coreapp.models import User, Category, SubCategory, Product, SendGridIntegration


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email")


class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SendGridIntegrationSerializer(ModelSerializer):
    class Meta:
        model = SendGridIntegration
        fields = "__all__"
