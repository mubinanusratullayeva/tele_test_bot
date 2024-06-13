from django.db import models


# Create your models here.
class User(models.Model):
    full_name = models.CharField(verbose_name="Full Name", max_length=100, null=True, blank=False)
    username = models.CharField(verbose_name="Username", max_length=20, unique=True, null=True)
    telegram_id = models.PositiveIntegerField(verbose_name="Telegram ID", max_length=20, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(verbose_name="Product name", max_length=50)
    photo = models.CharField(verbose_name="Photo file_id", max_length=200, null=True)
    price = models.DecimalField(verbose_name="Price", decimal_places=2, max_digits=8)
    description = models.TextField(verbose_name="About Product", max_length=3000, null=True)
    category_code = models.CharField(verbose_name="Category code", max_length=20)
    category_name = models.CharField(verbose_name="Category name", max_length=30)
    subcategory_code = models.CharField(verbose_name="Ost-category-code", max_length=20)
    subcategory_name = models.CharField(verbose_name="Ost-category-name", max_length=30)

    def __str__(self):
        return f"{self.id} - {self.product_name}"
