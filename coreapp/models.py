from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

    def change_password(self, new_password):
        self.set_password(new_password)
        self.save()

    def change_email(self, new_email):
        self.email = new_email
        self.save()


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class SendGridIntegration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.TextField()


# sendgridapi
# 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
