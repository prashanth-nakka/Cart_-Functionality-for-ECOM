from django.db import models
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"


class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.variant_name


class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.color_name}, {self.color_code}"


class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.size_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/products')
    price = models.CharField(max_length=20)
    stock = models.IntegerField(default=100)

    quantity_type = models.ForeignKey(
        QuantityVariant, blank=True, null=True, on_delete=models.PROTECT)
    color_type = models.ForeignKey(
        ColorVariant, blank=True, null=True, on_delete=models.PROTECT)
    size_type = models.ForeignKey(
        SizeVariant, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.product_name}, {self.category.category_name}, {self.price}, {self.stock}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='static/products')
