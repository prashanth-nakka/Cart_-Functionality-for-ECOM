from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import *
from home.models import *
# Create your views here.


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        cart = Cart.objects.filter(user=user, ordered=False).first()
        queryset = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user, ordered=False)
        product = Product.objects.get(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')
        print(quantity)
        cart_items = CartItem(cart=cart, user=user, product=product, price=price,
                              quantity=quantity)
        print(cart_items)
        cart_items.save()
        total_price = 0
        cart_items = CartItem.objects.filter(user=user, cart=cart.id)
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()
        return Response({"msg": "Items added to your cart"})

    def put(self, request, format=None):
        data = request.data
        cart_item = CartItem.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity = cart_item.quantity + quantity
        cart_item.save()
        return Response({'sucess': 'item-updated'})

    def delete(self, request, format=None):
        user = request.user
        data = request.data
        cart_item = CartItem.objects.get(id=data.get('id'))
        if cart_item:
            cart_item.delete()
            return Response({"msg": "Deleted Successfuly"})

        cart = Cart.objects.filter(user=user, ordered=False).first()
        queryset = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response(serializer.data)
