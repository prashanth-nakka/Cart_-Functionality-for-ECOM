from turtle import pos
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from home.models import Product
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self) -> str:
        return f"Username: {self.user.username} and Total: {self.total_price}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    # total_items = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"Product_Id: {self.product.id},\n Product_Name: {self.product.product_name},\n Quantity: {self.quantity},\n Total: {self.price}"


@receiver(post_save, sender=CartItem)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Product.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    # cart = Cart.objects.get(id=cart_items.cart.id)
    # cart.total_price = cart_items.price
    # cart.save()
    # print(cart_items.price)
    # total_cart_items = CartItem.objects.filter(user=cart_items.user)
    # cart_items.total_items = len(total_cart_items)
